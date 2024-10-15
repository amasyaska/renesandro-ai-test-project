# renesandro-ai-test-project
Test project for Renesandro AI
# setup
1. ```https://github.com/amasyaska/renesandro-ai-test-project.git```
2. create .env file in src/django-container, add SECRET_KEY, DJANGO_ALLOWED_HOSTS, DEBUG, SQL_ENGINE, SQL_DATABASE_NAME, SQL_DATABASE_USER, SQL_DATABASE_USER_PASSWORD, SQL_HOST, SQL_PORT
   ```
   SECRET_KEY={your SECRET_KEY here}
   DJANGO_ALLOWED_HOSTS={your Django ALLOWED_HOSTS here, separated by space}
   DEBUG={True or False}
   SQL_ENGINE=django.db.backends.postgresql
   SQL_DATABASE_NAME={your postgres database name}
   SQL_DATABASE_USER={your postgres user name}
   SQL_DATABASE_USER_PASSWORD={your postgres user password}
   SQL_HOST=db
   SQL_PORT=5432
   ```
3. create .env file in src/postgres-container, add POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB
   ```
   POSTGRES_USER={your postgres user name}
   POSTGRES_PASSWORD={your postgres user password}
   POSTGRES_DB={your postgres database name}
   ```
4. ```cd src```
5. ```docker compose build```
6. ```docker compose up -d```
7. go to ```localhost:8080```

# endpoints
  - /api/regitster POST, OPTIONS -- add user
  - /api/login POST, OPTIONS -- login user
  - /api/logout POST, OPTIONS -- login user
  - /api/token POST, OPTIONS -- get JWT
  - /api/token/refresh POST, OPTIONS -- refresh JWT

# implemented
- JWT Authentication
- Docker

# used
Nginx, Django, Django REST Framework, JWT authentication, Docker
