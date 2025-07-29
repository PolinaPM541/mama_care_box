# 🍼 Mama Care Box

FastAPI-додаток для товарів для мам та немовлят.

## 📚 Вимоги

- Python 3.11+
- Docker та Docker Compose (рекомендується)
- Git

## 🚀 Швидкий старт

1. Клонуйте репозиторій:
   ```bash
   https://github.com/PolinaPM541/mama_care_box.git
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


| Метод | URL | Опис |
|-------|-----|------|
| GET | `/docs` | Swagger UI документація |
| GET | `/redoc` | ReDoc документація |
| GET | `/openapi.json` | OpenAPI JSON документація |


## 📁 Структура проекту

mama_care_box/
├── api/                    # API маршрути
│   ├── v1/endpoints/      # Версія 1 API
│   │   ├── user.py        # Користувачі
│   │   ├── product.py     # Товари
│   │   └── basket.py      # Кошик
│   └── router.py          # Головний роутер
├── core/                  # Основні налаштування
│   └── config.py         # Конфігурація
├── models/               # SQLAlchemy моделі
│   ├── base.py          # Базова модель
│   ├── user.py          # Модель користувача
│   ├── product.py       # Модель товару
│   ├── basket.py        # Модель кошика
│   └── order.py         # Модель замовлення
├── repositories/         # Репозиторії для роботи з БД
├── services/            # Бізнес-логіка
├── schemas/             # Pydantic схеми
├── migrations/          # Alembic міграції
├── docker-compose.yml   # Docker Compose конфігурація
├── Dockerfile          # Docker образ
├── requirements.txt    # Python залежності
├── main.py            # Точка входу
└── .env               # Змінні середовища
```

## ⚙️ Конфігурація

### Змінні середовища (.env)

```bash
# База даних
DATABASE_URL=postgresql+asyncpg://user:password@host:port/dbname

# Google OAuth (опційно)
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret

# JWT секрет (у auth.py)
SECRET=your_jwt_secret_key
```

### Docker Compose

Файл `docker-compose.yml` налаштовано для:
- **web**: FastAPI додаток на порту 9000
- **db**: PostgreSQL 13 на порту 5432
- **volumes**: Збереження даних БД


## 📝 Ліцензія

MIT License

## 👨‍💻 Автор

InvisUA-creator

---

## 🚀 Швидкий старт

```bash
# 1. Клонування
git clone https://github.com/InvisUA-creator/mama_care_box.git
cd mama_care_box

# 2. Створення .env
echo "DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/mama_care_box
GOOGLE_CLIENT_ID=test_client_id
GOOGLE_CLIENT_SECRET=test_client_secret" > .env

# 3. Запуск
docker-compose up --build

# 4. Відкрити у браузері
# http://localhost:9000/docs
