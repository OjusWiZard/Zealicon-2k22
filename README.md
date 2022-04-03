# Zealicon 2k22

## How to setup development environment (Linux)
1. Clone this repository `git clone https://github.com/OjusWiZard/Zealicon-2k22.git`.
2. `cd Zealicon-2k22`.
3. Run `virtualenv venv`.
4. `source venv/bin/activate` to activate the virtual environment.
5. Run `pip install -r requirements.txt` to install the dependencies.
6. Run migrations using `python manage.py migrate`.
7. `python manage.py runserver` and you're ready.

## Adding evironment variables
1. Create a `.env` file.
2. Set environment variables as below
```sh
# General Settings

SERVER_HOST = ""
DJANGO_SECRET_KEY = ""
DEBUG = True
FRONTEND_HOST = "zealicon.in"


# Razorpay Payment Settings
FEE_AMOUNT = 100
KEY_ID = ""
KEY_SECRET = ""

# Email Settings

EMAIL_USE_TLS = False
EMAIL_HOST = ""
EMAIL_PORT = ""
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
DEFAULT_FROM_EMAIL = ""
```

## Launcing on Production using Docker
1. Create `.env` in root folder
3. Run `docker-compose up`.