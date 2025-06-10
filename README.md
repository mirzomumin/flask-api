# 📖 Flask Application — Dockerized Deployment

## 📦 Описание

Этот проект — backend-приложение на **Flask**, использующее **PostgreSQL** в качестве базы данных, **Alembic** для управления миграциями и деплоится с помощью **Docker Compose**.  
Автоматическая сборка и деплой настроены через **Jenkins Pipeline**.

---

## 📂 Структура проекта

```shell
flask-app
├── alembic
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
├── alembic.ini
├── app
│   ├── db.py
│   ├── models.py
│   └── routes.py
├── docker-compose.yml
├── Dockerfile
├── gunicorn.conf.py
├── Jenkinsfile
├── main.py
├── .gitignore
├── .env.example
└── requirements.txt
```

## 🚀 Запуск проекта

1. Клонирование проекта:
```shell
git clone https://github.com/mirzomumin/flask-app.git
```

2. Переход в директорию проекта:
```shell
cd flask-app
```

3. Копируем файл `.env.example` в новый файл `.env` (изменять значения переменных по необходимости):
```shell
cp .env.example .env
```

4. Запуск проекта при помощи docker:
```shell
docker compose up -d --build
```

## 📡 Примеры API-запросов

POST /submit
```shell
curl -X POST http://localhost:5000/submit -H "Content-Type: application/json" -d '{"name": "Mirzomumin", "score": 90}'
```

```shell
{"message":"Data saved successfully"}
```

GET /ping
```shell
curl -X GET http://localhost:5000/ping'
```

```shell
{"status":"ok"}
```

GET /results
```shell
curl -X GET http://localhost:5000/results'
```

```shell
[
  {"id":3,"name":"Mirzomumin","score":90,"timestamp":"2025-06-10T00:54:06.893973"}
  {"id":2,"name":"Kirill","score":88,"timestamp":"2025-06-10T00:35:13.622451"},
  {"id":1,"name":"Kirill","score":88,"timestamp":"2025-06-10T00:28:49.990504"}
]
```
