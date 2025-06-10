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
curl -X POST http://37.9.53.88:5000/submit -H "Content-Type: application/json" -d '{"name": "Mirzomumin", "score": 90}'
```

```shell
{"message":"Data saved successfully"}
```

GET /ping
```shell
curl -X GET http://37.9.53.88:5000/ping'
```

```shell
{"status":"ok"}
```

GET /results
```shell
curl -X GET http://37.9.53.88:5000/results'
```

```shell
[
  {"id":3,"name":"Mirzomumin","score":90,"timestamp":"2025-06-10T00:54:06.893973"}
  {"id":2,"name":"Kirill","score":88,"timestamp":"2025-06-10T00:35:13.622451"},
  {"id":1,"name":"Kirill","score":88,"timestamp":"2025-06-10T00:28:49.990504"}
]
```

## ⚙️ Как настроить Jenkins
1. Установить Jenkins и необходимые плагины:
- Docker plugin
- Docker Pipeline
- SSH Agent plugin
- Credentials Binding

3. Добавить креды:
- DockerHub Credentials: dockerhub-credentials (username/password)
- SSH Credentials: ssh-credentials-id (для деплоя на сервер)

4. Создать Pipeline job:
- В Jenkins → New Item → Pipeline
- В разделе Pipeline script from SCM указать:
- Git репозиторий
- Ветка
- Путь к Jenkinsfile (обычно в корне)
- Запустить билд.

## 🔄 Как работает CI/CD
Пайплайн реализован через Jenkinsfile и состоит из этапов:

- 📥 Checkout — забирает код из репозитория.

- 🐳 Build Docker Image — собирает образ приложения.

- ✅ Lint/Test — прогоняет линтер ruff.

- 📤 Push Docker Image — пушит образ на DockerHub.

- 📡 Deploy to Remote Server — подключается по SSH к серверу, обновляет образ и перезапускает контейнеры с помощью Docker Compose.
