# 🍼 Mama Care Box

FastAPI додаток товарів для мам та немовлят.

## 📚 Документація

[Документація FastAPI](https://fastapi.tiangolo.com/)

### Вимоги

- Python 3.11+
- Docker та Docker Compose
- Git

### Клонування репозиторію

```bash
git clone https://github.com/InvisUA-creator/mama_care_box.git
cd mama_care_box
```

## 🐳 Запуск через Docker (Рекомендовано)

### 1. Створіть файл `.env`

```bash
# Створіть файл .env у корені проекту
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/mama_care_box
GOOGLE_CLIENT_ID=test_client_id
GOOGLE_CLIENT_SECRET=test_client_secret
```

### 2. Запустіть проект

```bash
# Запуск усіх сервісів
docker-compose up --build

# Або у фоновому режимі
docker-compose up -d --build
```

### 3. Перевірте роботу

- **API**: http://localhost:9000
- **Документація**: http://localhost:9000/docs
- **Redoc**: http://localhost:9000/redoc

### Управління Docker контейнерами

```bash
# Зупинити всі сервіси
docker-compose down

# Переглянути логи
docker-compose logs

# Переглянути логи конкретного сервісу
docker-compose logs web
docker-compose logs db

# Перезапуск сервісу
docker-compose restart web

# Зупинка з видаленням томів
docker-compose down -v
```

## 💻 Локальний запуск

### 1. Створіть віртуальне середовище

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 2. Встановіть залежності

```bash
pip install -r requirements.txt
```

### 3. Налаштуйте базу даних

#### Варіант A: PostgreSQL

```bash
# Встановіть PostgreSQL локально
# Створіть базу даних mama_care_box

# У файлі .env
DATABASE_URL=postgresql+asyncpg://postgres:your_password@localhost:5432/mama_care_box
```

#### Варіант B: SQLite (для швидкого тестування)

```bash
# У файлі .env
DATABASE_URL=sqlite+aiosqlite:///./mama_care_box.db

# Встановіть драйвер
pip install aiosqlite
```

### 4. Виконайте міграції

```bash
# Створіть міграцію
alembic revision --autogenerate -m "Initial migration"

# Застосуйте міграції
alembic upgrade head
```

### 5. Запустіть сервер

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