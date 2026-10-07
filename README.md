<div align="center">

<img src="assets/readme/hero.gif" width="1200" alt="TEMP MAIL STUDIO — rotating 3D geometry" />

**[English](README.md) · [فارسی](README.fa.md)**

<img src="assets/readme/identity.svg" width="1200" alt="ai / English and Persian documentation" />

</div>

# TEMP MAIL STUDIO

A terminal tool for creating temporary inboxes through temp-mail.io, monitoring messages with background threads and extracting likely verification codes.

[GitHub](https://github.com/MOHAMMADREZAABEDINPOOR/email-generator) · [PIMX / Profile](https://github.com/MOHAMMADREZAABEDINPOOR) · [Static artwork](assets/readme/hero.png)

## Features

- Batch creation of temporary email accounts
- Threaded inbox monitoring and duplicate-message tracking
- English/Persian verification-code patterns
- Local JSON account persistence and timestamped logs

## Stack

| Tool | Version / source |
|---|---|
| requests>=2.32.3,<3 | `requirements.txt` |

## Getting started

Python 3; a desktop/Tk installation for Tkinter or turtle examples. Tkinter is provided by the Python installation, not pip. Legacy dependencies may need a compatible Python version.

```bash
git clone https://github.com/MOHAMMADREZAABEDINPOOR/email-generator.git
cd email-generator

python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1; macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python temp_email_generator.py
```

## Configuration

No standard environment template is defined. Standalone exercises need no external configuration; inspect any service constants or paths in the source before running.

## Usage

Run temp_email_generator.py and use its terminal menu to create inboxes or monitor saved accounts. Account tokens are stored locally in saved_emails_io.json and must remain private.

## Project structure

| Path | Role |
|---|---|
| [`assets/`](assets/) | Brand/media/README assets |
| [`temp_email_generator.py`](temp_email_generator.py) | Project entry/configuration file |

## Commands and checks

No automated test command is declared in a manifest. Verify behavior through a local example run.

## Deployment

Host a long-running bot process with environment secrets and private storage. Run a single polling instance. Check network access and dependency compatibility on the host.

## Limitations

The implementation calls an internal provider endpoint that may change without notice. Temporary inbox delivery and code extraction are best effort. Saved account files and logs are excluded from Git.

## Troubleshooting

- Missing packages: install dependencies using the project’s package manager.
- API/network failure: check the configured origin, provider and hosting bindings.
- Old assets: rebuild when a build script exists, then clear the browser cache.

## Contributing

Create a focused branch, verify the affected behavior and explain the change clearly. Keep private data, build outputs and local databases out of commits.

## License

No repository-level license file is included in this snapshot. Public visibility alone does not grant reuse rights; contact the repository owner for terms.

---

Part of **PIMX** · Documentation in English and Persian.
