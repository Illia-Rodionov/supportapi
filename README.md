# Terms of reference for the position of Python Developer Junior:

1. **Technologies:**
    Django + Django Rest Framework, JWT авторизация, PostgreSQL, Docker (Docker-compose), PyTests, Celery, Redis, flake8,
    isort
2. **Description of the business task:** 

Basic:
**Support service:**
   1. The user writes a ticket and sends it.
   2. Support sees resolved, unresolved and frozen tickets (all in fact), can respond to them.
   3. The user can view the answer of the support, and add a new message (the support will answer it).
   4. Support can change ticket statuses.

Additionally:
Sending status change notifications to email

# Run the project locally
1. **Fill in .env file, edit .env example**

2. **Build the containers**
```shell
docker-compose build
```
3. **Run the containers**
```shell
docker-compose up -d
```
4. **Track the logs**
```shell
docker-compose logs -f 
```
5. **Create superuser**
```shell
docker-compose exec app python manage.py createsuperuser --username admin
```