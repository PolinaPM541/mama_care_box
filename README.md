# 🍼 Mama Care Box

FastAPI-додаток для товарів для мам та немовлят.

## 📚 Вимоги

- Python 3.11+
- Docker та Docker Compose (рекомендується)
- Git

## 🚀 Швидкий старт

1. Клонуйте репозиторій:
   ```bash
   git clone https://github.com/PolinaPM541/mama_care_box.git
   cd mama_care_box
   ```

2. Скопіюйте `env_example` для свого проекту та введіть свої дані, приклад: 
   ```bash
   MODE=your_mode
   COOKIE_MAX_AGE=your_time
   JWT_LIFETIME_SECONDS=your_time
   DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/mama_care_box
   TEST_DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/test_mama_care_box
   GOOGLE_OAUTH2_CLIENT_ID=test_client_id
   GOOGLE_OAUTH2_CLIENT_SECRET=test_client_secret
   FACEBOOK_OAUTH2_CLIENT_ID=test_client_id
   FACEBOOK_OAUTH2_CLIENT_SECRET=test_client_secret
   SECRET=your_jwt_secret_key

   ```

3. Запустіть через Docker:
   ```bash
   docker-compose -f docker-compose.test.yml up --build -d
   ```

4. Відкрийте API: [http://localhost:9000/docs](http://localhost:9000/docs)

## 📚 API Документація


| Метод | URL | Опис |
|-------|-----|------|
| GET | `/docs` | Swagger UI документація |
| GET | `/redoc` | ReDoc документація |
| GET | `/openapi.json` | OpenAPI JSON документація |


## 📁 Структура проекту

mama_care_box/
|   .env # Змінні середовища
|   .env_dev # Змінні середовища
|   .pre-commit-config.yaml # конфігуратор для рефакторінгу
|   docker-compose.yml  # Docker Compose конфігурація
|   Dockerfile # Docker образ
|   main.py # Точка входу
|   pyproject.toml # рефакторінг настройки
|   pytest.ini # конфігуратор настройки тестів
|   requirements.txt # залежності
+---app # API маршрут
|   |   config.py # Конфігурація
|   |   conftest.py # Конфіг для тестів
|   |   database.py # Підключення к бд
|   |   exceptions.py # особливі винятки
|   |   router.py # шлях
|   |   responses_api # коди та опис  для відповіді
|   |
|   +---Basket
|   |   |   dao.py # логика бд
|   |   |   dependencies.py # Залежності для basket
|   |   |   models.py # модель для бд
|   |   |   router.py # шлях
|   |   |   schemas.py # Pydantic схема
|   |   |
|   |
|   +---Categories
|   |   |   dao.py # логика бд
|   |   |   models.py # модель для бд
|   |   |   router.py # шлях
|   |   |   schemas.py #  Pydantic схема
|   |   |
|   +---dao
|   |   |   base.py
|   +---Product
|   |   |   dao.py # логика бд
|   |   |   models.py # модель бд
|   |   |   router.py # шлях
|   |   |   schemas.py #  Pydantic схема
|   +---tests
|   |   |   conftest.py #
|   |   |   mock_basket.json
|   |   |   mock_category.json
|   |   |   mock_order.json
|   |   |   mock_order_item.json
|   |   |   mock_product.json
|   |   |   mock_subcategory.json
|   |   |   mock_users.json
|   |   |
|   |   +---integration_tests
|   |   |   \---test_dao
|   |   |       |   test_models_basket.py
|   |   |
|   |   +---unit_tests
|   |      +---test_basket
|   |     |   |   test_api_basket.py
|   |     +---test_categorie
|   |     |   |   test_categorie_.py
|   |     +---test_product
|   |     |   |   test_product_.py
|   |     \---test_user
|   |         |   test_auth_user_api.py
|   |
    +---user
       |   auth.py # голова аутентифікація
       |   dao.py # логика бд
       |   dependencies.py # залежності для утентифікації
       |   models.py # модель бд
       |   router.py # шлях
       |   schemas.py # Pydantic схема

```

## 🚀 Швидкий старт

```bash
# 1. Клонування
git clone https://github.com/PolinaPM541/mama_care_box.git
cd mama_care_box

# 2. Створення .env
echo "
   MODE=your_mode
   COOKIE_MAX_AGE=your_time
   JWT_LIFETIME_SECONDS=your_time
   DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/mama_care_box
   TEST_DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/test_mama_care_box
   GOOGLE_CLIENT_ID=test_client_id
   GOOGLE_CLIENT_SECRET=test_client_secret
   SECRET=your_jwt_secret_key
   FACEBOOK_OAUTH2_CLIENT_ID=test_client_id
   FACEBOOK_OAUTH2_CLIENT_SECRET=test_client_secret
   " > .env

# 3. Запуск
docker-compose -t docker-compose.test.yml  up --build

# 4. Відкрити у браузері
# http://localhost:9000/docs
