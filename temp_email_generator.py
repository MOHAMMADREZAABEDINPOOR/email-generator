import requests
import time
import threading
import re
import json
import os
from datetime import datetime

BASE_URL = "https://api.internal.temp-mail.io/api/v3"
SAVE_FILE = "saved_emails_io.json"
LOG_FILE = "emails_log_io.txt"

class Colors:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

def log(msg, color=Colors.RESET):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full = f"[{timestamp}] {msg}"
    print(f"{color}{full}{Colors.RESET}")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(full + "\n")

def save_accounts(accounts):
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(accounts, f, indent=2, ensure_ascii=False)
    log(f"✅ {len(accounts)} ایمیل ذخیره شد", Colors.GREEN)

def load_accounts():
    if not os.path.exists(SAVE_FILE):
        return []
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def create_email():
    try:
        r = requests.post(f"{BASE_URL}/email/new", 
                          headers={"Content-Type": "application/json"},
                          json={},
                          timeout=15)
        r.raise_for_status()
        data = r.json()
        email = data.get("email")
        token = data.get("token")
        if email and token:
            return {
                "email": email,
                "token": token,
                "created_at": datetime.now().isoformat(),
                "provider": "temp-mail.io"
            }
    except Exception as e:
        log(f"خطا در ساخت ایمیل: {e}", Colors.RED)
    return None

def get_messages(email, token):
    try:
        headers = {"Authorization": f"Bearer {token}"}
        r = requests.get(f"{BASE_URL}/email/{email}/messages", 
                         headers=headers, 
                         timeout=12)
        if r.status_code == 200:
            return r.json()  # لیست پیام‌ها
        else:
            log(f"وضعیت غیرعادی: {r.status_code} - {r.text[:200]}", Colors.YELLOW)
    except Exception as e:
        log(f"خطا در گرفتن پیام‌ها: {e}", Colors.RED)
    return []

def extract_code(text):
    if not text:
        return None
    clean = re.sub(r'<[^>]+>', ' ', str(text))
    clean = re.sub(r'\s+', ' ', clean)

    patterns = [
        r'(?:code|کد|otp|verification|confirm|pin|token)[^\d]{0,30}(\d{4,8})',
        r'(\d{4,8})[^\d]{0,20}(?:code|کد|otp|verification)',
        r'\b(\d{6})\b',
        r'\b(\d{4,8})\b',
    ]
    for p in patterns:
        m = re.search(p, clean, re.IGNORECASE)
        if m:
            code = m.group(1)
            if code not in ["2023", "2024", "2025", "2026"]:
                return code
    return None

def monitor_one(account, stop_event, seen):
    email = account["email"]
    token = account["token"]
    log(f"👂 گوش دادن به: {email}", Colors.BLUE)

    while not stop_event.is_set():
        try:
            messages = get_messages(email, token)
            
            if not isinstance(messages, list):
                time.sleep(8)
                continue

            for msg in messages:
                # ساخت آیدی یکتا
                msg_id = str(msg.get("id") or msg.get("_id") or msg.get("created_at") or "")
                if not msg_id:
                    msg_id = str(hash(str(msg)))

                if email not in seen:
                    seen[email] = set()
                if msg_id in seen[email]:
                    continue
                seen[email].add(msg_id)

                subject = msg.get("subject", "") or ""
                body = msg.get("body_text") or msg.get("body") or msg.get("text") or msg.get("body_html") or msg.get("html") or ""
                
                # بعضی وقت‌ها محتوا توی فیلدهای دیگه است
                if not body:
                    body = str(msg)

                full = f"{subject}\n{body}"
                code = extract_code(full)

                log("=" * 55, Colors.CYAN)
                log(f"📧 ایمیل جدید برای: {email}", Colors.CYAN)
                log(f"موضوع: {subject}", Colors.CYAN)

                if code:
                    log(f"✅✅ کد تأیید: {code}", Colors.GREEN + Colors.BOLD)
                else:
                    log("⚠️ کد پیدا نشد. محتوای ایمیل:", Colors.YELLOW)
                    log(str(body)[:600], Colors.YELLOW)

                log("=" * 55, Colors.CYAN)

            time.sleep(8)
        except Exception as e:
            log(f"خطا در مانیتورینگ {email}: {e}", Colors.RED)
            time.sleep(12)

def create_batch(count):
    accounts = load_accounts()
    new_ones = []

    log(f"شروع ساخت {count} ایمیل با temp-mail.io ...", Colors.BLUE)

    for i in range(count):
        acc = create_email()
        if acc:
            accounts.append(acc)
            new_ones.append(acc)
            log(f"[{i+1}/{count}] {acc['email']}", Colors.GREEN)
        else:
            log(f"[{i+1}/{count}] ناموفق", Colors.RED)
        time.sleep(1.3)

    save_accounts(accounts)
    log(f"\n✅ {len(new_ones)} ایمیل ساخته شد.", Colors.GREEN)
    return new_ones

def start_monitor(accounts=None):
    if accounts is None:
        accounts = load_accounts()

    if not accounts:
        log("هیچ ایمیلی وجود ندارد!", Colors.RED)
        return

    log(f"شروع مانیتورینگ {len(accounts)} ایمیل... (Ctrl+C برای توقف)", Colors.MAGENTA)

    stop = threading.Event()
    seen = {}
    threads = []

    for acc in accounts:
        t = threading.Thread(target=monitor_one, args=(acc, stop, seen), daemon=True)
        t.start()
        threads.append(t)
        time.sleep(0.3)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        log("\nدر حال توقف...", Colors.YELLOW)
        stop.set()
        time.sleep(2)
        log("متوقف شد.", Colors.GREEN)

def main():
    while True:
        print("\n" + "=" * 55)
        print(f"{Colors.BOLD}Temp-Mail.io Generator + Monitor{Colors.RESET}")
        print("=" * 55)
        print("1. ساخت ایمیل جدید")
        print("2. لود لیست قبلی و مانیتور")
        print("3. نمایش لیست ذخیره‌شده")
        print("4. ساخت + مانیتور همزمان")
        print("5. خروج")
        print("=" * 55)

        choice = input("انتخاب (1-5): ").strip()

        if choice == "1":
            try:
                n = int(input("چند تا؟ "))
                if n > 0:
                    create_batch(n)
            except:
                print("عدد معتبر وارد کن.")

        elif choice == "2":
            start_monitor()

        elif choice == "3":
            accs = load_accounts()
            if not accs:
                print("لیست خالی است.")
            else:
                print(f"\n{len(accs)} ایمیل:\n")
                for i, a in enumerate(accs, 1):
                    print(f"{i}. {a['email']}")

        elif choice == "4":
            try:
                n = int(input("چند تا بسازم و مانیتور کنم؟ "))
                if n > 0:
                    news = create_batch(n)
                    if news:
                        start_monitor(news)
            except:
                print("عدد معتبر وارد کن.")

        elif choice == "5":
            break
        else:
            print("گزینه نامعتبر.")

if __name__ == "__main__":
    main()