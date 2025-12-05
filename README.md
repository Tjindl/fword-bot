# 🤖 Tushar's Portfolio Bot (fword-bot)

> "You asked for real, so here is the real info without the fluff."

A Telegram bot that serves as an interactive portfolio and resume. Built with Python and `python-telegram-bot`, this bot allows users to explore my bio, tech stack, projects, and contact information through a clean, button-based interface.

## ✨ Features

- **Interactive Menu:** Navigate through different sections using inline buttons.
- **Bio Section:** A quick introduction to who I am.
- **Tech Stack:** A showcase of my skills in Languages, AI/ML, Web, and DevOps.
- **Projects:** Direct links to my top projects like Code Lantern, Resume Optimizer, and more.
- **Vibe Check:** A fun little section to show some personality.
- **Contact Info:** Easy access to my Email, GitHub, and Portfolio website.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Framework:** [python-telegram-bot](https://python-telegram-bot.org/)
- **Environment Management:** `python-dotenv`
- **Logging:** Standard Python `logging` module

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- A Telegram Bot Token (Get one from [@BotFather](https://t.me/BotFather))

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Tjindl/fword-bot.git
   cd fword-bot
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables:**
   Create a `.env` file in the root directory and add your bot token:
   ```env
   BOT_TOKEN=your_telegram_bot_token_here
   ```

### Running the Bot

Start the bot with:
```bash
python main.py
```

You should see:
```
Bot is polling... (Press Ctrl+C to stop)
```

Now, open Telegram and search for your bot. Send `/start` to begin interacting!

## 📂 Project Structure

- `main.py`: The entry point of the application. Handles bot initialization, command handlers, and callback queries.
- `content.py`: Stores all the text content for the bot (Bio, Skills, Projects, etc.) to keep `main.py` clean.
- `.env`: (Not committed) Stores sensitive configuration like the Bot Token.

## 🤝 Contact

**Tushar Jindal**

- 📧 Email: [tushar.bzp05@gmail.com](mailto:tushar.bzp05@gmail.com)
- 🐙 GitHub: [@Tjindl](https://github.com/Tjindl)
- 🌐 Portfolio: [tjindl.github.io](https://tjindl.github.io/portfolio_new/)

---
*Built with ❤️ and Python.*