# djan_test
ReachLocal Japan Programming Test

## Copy

Use [Git](https://github.com/bowonwit7447/djan_test.git) to copy the repository on Git.
```bash
git clone https://github.com/bowonwit7447/djan_test.git
```

## Installation

Use the [virtualenv](https://pypi.org/project/virtualenv/) to generate Vitual Envelopment.

```bash
pip install virtualenv
```

Then

```bash
virtualenv djan_test

cd djan_test

Scripts\activate

pip install -r requirements.txt
```

## Setup Server

Use this command to create db.sqlite3
```bash
python manage.py makemigrations

python manage.py migrate
```

Then, use this command for create superuser to login in admin display [https://localhost:8000/admin]
```bash
python manage.py createsuperuser
```
And then, enter Username, Email, Passwords

Use this command to start server
```bash
python manage.py runserver
```

## Usage

- Go to [Get News](https://localhost:8000/get_news) tab. Enter API key that you have.

- Click [Request]() button. The display will show news list of respond.

- Click [Save]() button to save the news list to Database.

- Then, go to [Home](https://localhost:8000/home) tab to display last 20 item of news list.

- Please enjoin!

## License
None