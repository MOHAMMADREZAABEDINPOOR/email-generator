<div align="center">

<img src="assets/readme/hero.gif" width="1200" alt="TEMP MAIL STUDIO — rotating 3D geometry" />

**[English](README.md) · [فارسی](README.fa.md)**

<img src="assets/readme/identity.svg" width="1200" alt="ai / English and Persian documentation" />

</div>

# TEMP MAIL STUDIO

ابزار ترمینال برای ساخت صندوق موقت با temp-mail.io، پایش پیام با نخ پس‌زمینه و استخراج کدهای احتمالی تأیید.

[GitHub](https://github.com/MOHAMMADREZAABEDINPOOR/email-generator) · [PIMX / Profile](https://github.com/MOHAMMADREZAABEDINPOOR) · [بنر ثابت](assets/readme/hero.png)

## امکانات

- ساخت گروهی حساب ایمیل موقت
- پایش چندنخی صندوق و تشخیص پیام تکراری
- الگوهای کد تأیید انگلیسی و فارسی
- ذخیره حساب در JSON محلی و لاگ زمان‌دار

## پشته فنی

| ابزار | نسخه یا منبع |
|---|---|
| requests>=2.32.3,<3 | `requirements.txt` |

## شروع کار

Python 3 و محیط دسکتاپ برای پروژه‌های Tkinter/Turtle؛ Tkinter از اجزای نصب Python است و با pip نصب نمی‌شود. برای وابستگی‌های قدیمی از نسخه Python سازگار استفاده کنید.

```bash
git clone https://github.com/MOHAMMADREZAABEDINPOOR/email-generator.git
cd email-generator

python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1; macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python temp_email_generator.py
```

## تنظیمات

فایل محیط استاندارد تعریف نشده است. برای تمرین‌های مستقل تنظیم خارجی لازم نیست؛ اگر در کد ثابت‌های سرویس یا مسیر وجود دارد، آن‌ها را پیش از اجرا بررسی کنید.

## استفاده

temp_email_generator.py را اجرا و از منوی ترمینال برای ساخت صندوق یا پایش حساب ذخیره‌شده استفاده کنید. توکن حساب در saved_emails_io.json محلی ذخیره می‌شود و باید خصوصی بماند.

## ساختار پروژه

| مسیر | نقش |
|---|---|
| [`assets/`](assets/) | فایل برند، رسانه و README |
| [`temp_email_generator.py`](temp_email_generator.py) | فایل ورودی یا تنظیم پروژه |

## فرمان‌ها و بررسی

فرمان آزمون خودکار در manifest تعریف نشده است. اجرای محلی و بررسی رفتار نمونه را انجام دهید.

## استقرار

ربات را با فرایند پایدار، اسرار محیطی و فضای ذخیره خصوصی میزبانی کنید. تنها یک نمونه polling اجرا کنید. تنظیم شبکه و نسخه وابستگی را روی هاست بررسی کنید.

## محدودیت‌ها

کد از مسیر داخلی سرویس استفاده می‌کند که ممکن است بدون اطلاع تغییر کند. دریافت ایمیل و استخراج کد قطعی نیست. فایل حساب و لاگ از Git کنار گذاشته شده‌اند.

## رفع مشکل

- پکیج غایب: وابستگی را با مدیر پکیج پروژه نصب کنید.
- خطای API یا شبکه: آدرس، سرویس و اتصال میزبانی را بررسی کنید.
- فایل قدیمی: در صورت وجود اسکریپت ساخت، build و کش مرورگر را تازه کنید.

## مشارکت

برای تغییر، شاخه مستقل بسازید، رفتار فعلی را بررسی کنید و توضیح روشن همراه تغییر بفرستید. اطلاعات خصوصی، خروجی build و دیتابیس محلی را commit نکنید.

## مجوز

فایل مجوز در این نسخه موجود نیست. نمایش عمومی کد به‌تنهایی مجوز استفاده مجدد نیست؛ برای شرایط استفاده با مالک مخزن هماهنگ کنید.

---

ساخته‌شده در مجموعه **PIMX** · مستندات فارسی و انگلیسی.
