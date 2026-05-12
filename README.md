# Dutch Home Finder

A small service that monitors new property listings on Funda, stores them in a database, and sends Telegram notifications.

---

## Features

- Scrapes the latest listings from Funda.
- Detects only listings that are not yet stored.
- Filters out sold or outdated properties.
- Sends formatted notifications to Telegram.
- Persists listings in PostgreSQL.
- Uses asynchronous I/O where it makes sense.

---

## Tech stack

| Technology   | Purpose                     |
|-------------|-----------------------------|
| Python 3.13 | Runtime                     |
| SQLAlchemy  | ORM                         |
| Alembic     | Database migrations         |
| PostgreSQL  | Database                    |
| Pydantic    | Data validation             |
| aiogram     | Telegram bot / notifications |
| FastAPI     | Optional HTTP API layer     |
| asyncpg     | Async PostgreSQL driver     |

---

## Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables (for example via a `.env` file in the project root):

   ```env
   DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dutch_home_finder
   FUNDA_API_KEY=...
   TELEGRAM_BOT_TOKEN=...
   TELEGRAM_CHAT_ID=...
   ```

4. Apply database migrations:

   ```bash
   alembic upgrade head
   ```

---

## Running

Run the scraper:

```bash
python main.py
```

This will:

1. Fetch current listings from Funda.
2. Determine which ones are new.
3. Load full details for new listings.
4. Filter by status and publication date.
5. Save new listings to the database.
6. Send notifications to Telegram.

You can schedule this command with cron, systemd, or any other job scheduler.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.