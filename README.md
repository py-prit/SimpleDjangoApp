# Project Setup Instructions

1. Make sure Python 3.10 is installed.

```
python3 --version
```

2. Create virtual environment

```
python3 -m venv env
```

3. Install all requirements in environment.

```
pip install -r requirements.txt
```

4. Create .env file and add following variables in that file

```
DB_NAME <DATABASE_NAME>
DB_USER <DATABASE_USERNAME>
DB_PASSWORD <DATABASE_PASSWORD>
DB_HOST <DATABASE_HOST_NAME>
EMAIL_HOST_USER <Email address to be used for sending email>
EMAIL_HOST_PASSWORD <Password of the email address used for sending email>
```

5. Apply migration changes to your database

```
python manage.py migrate
```

6. Collect Static files

```
python manage.py collectstatic --no-input
```

7. Run Django Server

```
python manage.py runserver
```