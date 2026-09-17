# 04 Production Service

Учебный стенд с FastAPI, Redis, фоновой очередью и Docker Compose. Он показывает границы сервисов, а не заменяет полноценную облачную инфраструктуру.

## Запуск

```bash
cp .env.example .env
docker compose up --build
```

Проверки:

```bash
curl http://127.0.0.1:8000/health
curl -X POST http://127.0.0.1:8000/jobs -H 'content-type: application/json' -d '{"name":"report"}'
```

В production нужно добавить Postgres, авторизацию, retry policy, метрики, TLS, secrets manager и миграции.
