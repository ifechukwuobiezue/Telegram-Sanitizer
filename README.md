# Telegram Sanitizer Tools

A collection of Python scripts to help you clean up your Telegram account, such as leaving groups, deleting empty/system-only chats, and more.

---

## Features
- Leave all groups
- Delete all empty/system-only chats
- (More scripts can be added)

---

## Prerequisites

- **Python 3.7+** installed on your system ([Download Python](https://www.python.org/downloads/))
- A Telegram account
- Telegram API credentials (API ID and API Hash)

---

## Getting Your Telegram API Keys

1. Go to [my.telegram.org](https://my.telegram.org/)
2. Log in with your phone number
3. Click on "API development tools"
4. Fill in the required fields (app title, short name, etc.)
5. After submitting, you will get your **API ID** and **API Hash**

---

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/telegram-sanitizer.git
   cd telegram-sanitizer
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the project directory:**
   ```
   API_ID=your_api_id
   API_HASH=your_api_hash
   ```
   Replace `your_api_id` and `your_api_hash` with the values you got from my.telegram.org.

---

## Usage

### 1. **Delete Empty/System-Only Chats**
   ```bash
   python emptychats.py
   ```
   - This will delete all chats with no messages or only system messages (e.g., "User joined Telegram").

### 2. **Leave All Groups**
   ```bash
   python leavegroups.py
   ```
   - This will leave all group chats you are a member of.

---

## Notes
- Your `.env` file is **not** tracked by git (see `.gitignore`).
- Your credentials are only used locally and are not shared.
- You may be prompted for a login code the first time you run a script.

---

## For Non-Technical Users
- If you want a user-friendly app (no command line), stay tuned! A packaged version with a graphical interface is in the works.

---

## Troubleshooting
- If you get errors about missing modules, make sure you installed all dependencies with `pip install -r requirements.txt`.
- If you get authentication errors, double-check your API ID and API Hash in the `.env` file.

---

## License
MIT 