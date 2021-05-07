# P11_pur_beurre_V2
(Openclassrooms) Project 11 : Maintain and add features to a Django app

### Context
This project is related to the [Pur Beurre project](https://github.com/Lamia7/P8_pur_beurre) a web app to help you find a healthier substitute of a product you like eating. 😋

In this second version of the app, I am adding new features.

This project is part of my training at [Openclassrooms](https://openclassrooms.com/fr/).

### Installation and configuration 💻
- Create and activate virtual environment : `pipenv shell` 
- Install packages with pipenv : `pipenv install`
_If you need to install pipenv : (with pip for Linux) `pip3 install pipenv` (with brew on Mac) `brew install pipenv`
- Create your own .env file with environment variables that will be used by [dotenv](https://pypi.org/project/python-dotenv/) library
- Create a superuser : `python3 manage.py createsuperuser`
- `createdb <db_name>`
- Check the database PORT
- Launch the migration : `python3 manage.py migrate`
- Launch the command that feeds the database : `python3 manage.py feed_db`


**Clone the repository from Github by running this command:**

`git clone https://github.com/Lamia7/P8_pur_beurre.git`

**Execute with a virtual environment:**
Create a virtual environment: `pipenv shell` <br>
_If you need to install pipenv : (with pip for Linux) `pip3 install pipenv` (with brew on Mac) `brew install pipenv` <br>
Activate the virtual environment: `pipenv shell` or `source venv/bin/activate` <br>
First time: install dependencies : `pipenv install` or `pip3 install requirements.txt`

Run the application: `python3 manage.py runserver` and go to your localhost : `http://127.0.0.1:8000/`

(To deactivate the virtual environment, run this command: `exit`)

### New features added 📋
+ ...
+ ...

### Checklist 📝
- [ ] ...
- [ ] Added a functional test with Selenium
- [ ] Check PEP8 with flake8 and refacto with black + manually
- [ ] Deploy

### Tests 🧪
- Launches the unit tests : `coverage run --source='.' manage.py test`
- Display the coverage report : `coverage report`
- Display the html coverage report details : `coverage html`
- Launches the functional test with Selenium : `./manage.py test tests.users.functional_tests`
### Ressources used to create this program 🔧
***BACK***
- Language : Python 3.8
- Framework : Django 3.2

***DATABASE***
- PostgreSQL 13.2

***FRONT***
- Languages : Javascript, HTML5 & CSS3
- Frameworks : Bootstrap 4

***EXTERNAL RESSOURCES***
- Web server /  HTTP server : [Nginx](https://www.nginx.com/)
- HTTP/WSGI server : [Gunicorn](https://gunicorn.org/)
- REST API : [OpenFoodFacts](https://fr.openfoodfacts.org/)

### Author 📝
[Lamia EL RALIMI](https://github.com/Lamia7)