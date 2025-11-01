
FROM python:3.11-slim


WORKDIR /app


COPY requirements_dev.txt .

RUN pip install --no-cache-dir -r requirements_dev.txt && \
    pip show gunicorn || { echo "gunicorn not installed"; exit 1; }



COPY . .

EXPOSE 9000


HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:9000/docs || exit 1


CMD ["gunicorn", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:9000"]
