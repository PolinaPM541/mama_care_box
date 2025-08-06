# Використовуємо легкий базовий образ Python 3.11
FROM python:3.11-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо requirements.txt
COPY requirements.txt .
# Встановлюємо залежності та перевіряємо, що gunicorn встановлено
RUN pip install --no-cache-dir -r requirements.txt && \
    pip show gunicorn || { echo "gunicorn not installed"; exit 1; }

# Копіюємо решту файлів проєкту
COPY . .

# Створюємо некритичного користувача для безпеки
RUN useradd -m appuser
USER appuser

# Відкриваємо порт 9000 для FastAPI
EXPOSE 9000

# Додаємо перевірку здоров’я
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:9000/docs || exit 1

# Запускаємо gunicorn з Uvicorn для продакшену
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:9000"]
