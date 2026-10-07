<div align="center">

<img src="assets/readme/hero.gif" width="1200" alt="TEMP MAIL STUDIO: an open inbox receiving a verification-code card" />

**[English](README.md) · [فارسی](README.fa.md)**

</div>

# 📬 TEMP MAIL STUDIO

A terminal tool for creating temporary inboxes through temp-mail.io, monitoring messages with background threads and extracting likely verification codes.

[GitHub](https://github.com/MOHAMMADREZAABEDINPOOR/email-generator) · [PIMX / Profile](https://github.com/MOHAMMADREZAABEDINPOOR) · [Static artwork](assets/readme/hero.png)

| At a glance | Details |
|:---|:---|
| 📬 Experience | Terminal inbox utility |
| 🧰 Built with | `requests>=2.32.3,<3` |
| 🌐 Documentation | [English](README.md) · [فارسی](README.fa.md) |

[✨ Features](#features) · [🚀 Getting started](#getting-started) · [⚙️ Configuration](#configuration) · [🌍 Deployment](#deployment)

---

<a id="features"></a>

## ✨ Features

| Area | Included capability |
|:---|:---|
| 👤 Accounts | Batch creation of temporary email accounts |
| ⚡ Workflow | Threaded inbox monitoring and duplicate-message tracking |
| 🌐 Experience | English/Persian verification-code patterns |
| 👤 Accounts | Local JSON account persistence and timestamped logs |

<a id="stack"></a>

## 🧰 Stack

| Tool | Version / source |
|---|---|
| requests>=2.32.3,<3 | `requirements.txt` |

<a id="getting-started"></a>

## 🚀 Getting started

Python 3; a desktop/Tk installation for Tkinter or turtle examples. Tkinter is provided by the Python installation, not pip. Legacy dependencies may need a compatible Python version.

```bash
git clone https://github.com/MOHAMMADREZAABEDINPOOR/email-generator.git
cd email-generator

python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1; macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python temp_email_generator.py
```

<a id="configuration"></a>

## ⚙️ Configuration

No standard environment template is defined. Standalone exercises need no external configuration; inspect any service constants or paths in the source before running.

<a id="usage"></a>

## 🎯 Usage

Run temp_email_generator.py and use its terminal menu to create inboxes or monitor saved accounts. Account tokens are stored locally in saved_emails_io.json and must remain private.

<a id="project-structure"></a>

## 🗂️ Project structure

| Path | Role |
|---|---|
| [`assets/`](assets/) | Brand/media/README assets |
| [`temp_email_generator.py`](temp_email_generator.py) | Project entry/configuration file |

<a id="commands-and-checks"></a>

## 🧪 Commands and checks

No automated test command is declared in a manifest. Verify behavior through a local example run.

<a id="deployment"></a>

## 🌍 Deployment

Host a long-running bot process with environment secrets and private storage. Run a single polling instance. Check network access and dependency compatibility on the host.

<a id="limitations"></a>

## 📌 Limitations

The implementation calls an internal provider endpoint that may change without notice. Temporary inbox delivery and code extraction are best effort. Saved account files and logs are excluded from Git.

<a id="troubleshooting"></a>

## 🛠️ Troubleshooting

- Missing packages: install dependencies using the project’s package manager.
- API/network failure: check the configured origin, provider and hosting bindings.
- Old assets: rebuild when a build script exists, then clear the browser cache.

<a id="contributing"></a>

## 🤝 Contributing

Create a focused branch, verify the affected behavior and explain the change clearly. Keep private data, build outputs and local databases out of commits.

<a id="license"></a>

## 📄 License

No repository-level license file is included in this snapshot. Public visibility alone does not grant reuse rights; contact the repository owner for terms.

---

Part of **PIMX** · Documentation in English and Persian.

---

<div align="center">

📬 **TEMP MAIL STUDIO** · [English](README.md) · [فارسی](README.fa.md)

</div>
