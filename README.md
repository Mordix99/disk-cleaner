# Disk Cleaner & Maintenance Tool

A practical Python utility designed to automate disk cleanup by scanning, calculating reclaimable space, and safely removing temporary files and application caches based on a JSON configuration.

---

## 🚀 Features

- **Environment Variables Support**: Expands native system variables (e.g. `%TEMP%`, `%APPDATA%`) automatically.
- **Pre-execution Summary**: Scans recursively (`rglob`) and reports total file counts and reclaimable space in MB before performing any actions.
- **Interactive Safety Confirmation**: Prompts the user for confirmation before executing deletions to prevent accidental data loss.
- **Graceful Error Handling**: Catches file access and permission errors (`OSError`) without crashing the script.
- **Zero External Dependencies**: Built strictly using standard Python libraries.

---

## 🛠️ Technologies

- **Python 3**
- **Standard Libraries**: `pathlib`, `os`, `json`

---

## ⚙️ Configuration

Target directories are managed via `config.json`:

```json
{
  "target_directories": [
    "%TEMP%",
    "%APPDATA%/discord/Cache"
  ]
}
```
## USAGE 

```powershell
# Run the script directly
python cleaner.py
```