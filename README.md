# 🍼 Mama Care Box

FastAPI-додаток для товарів для мам та немовлят.

## 📚 Вимоги

- Python 3.11+
- Docker та Docker Compose (рекомендується)
- Git

## 🚀 Швидкий старт

1. Клонуйте репозиторій:
   ```bash
   git clone https://github.com/InvisUA-creator/mama_care_box.git
   cd mama_care_box
   ```

2. Створіть `.env`:
   ```bash
   DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/mama_care_box
   GOOGLE_CLIENT_ID=test_client_id
   GOOGLE_CLIENT_SECRET=test_client_secret
   SECRET=your_jwt_secret_key
   ```

3. Запустіть через Docker:
   ```bash
   docker-compose up --build
   ```

4. Відкрийте API: [http://localhost:9000/docs](http://localhost:9000/docs)

## 💻 Локальний запуск

1. Створіть та активуйте віртуальне середовище:
   ```bash
   python -m venv venv
   # Windows: venv\Scripts\activate
   # macOS/Linux: source venv/bin/activate
   ```

2. Встановіть залежності:
   ```bash
   pip install -r requirements.txt
   ```

3. Налаштуйте базу даних:
   - **PostgreSQL**: `DATABASE_URL=postgresql+asyncpg://postgres:your_password@localhost:5432/mama_care_box`
   - **SQLite**: `DATABASE_URL=sqlite+aiosqlite:///./mama_care_box.db` та `pip install aiosqlite`

4. Виконайте міграції:
   ```bash
   alembic revision --autogenerate -m "Initial migration"
   alembic upgrade head
   ```

5. Запустіть сервер:
   ```bash
   uvicorn main:app --reload --port 9000
   ```

## 📚 API Документація

- **Swagger UI**: `/docs`
- **ReDoc**: `/redoc`

## 🐳 Управління Docker

- Зупинити: `docker-compose down`
- Логи: `docker-compose logs [web|db]`

## About

FastAPI-додаток для управління товарами для мам та немовлят.

© 2025 GitHub, Inc.