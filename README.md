# Framework - Django Boilerplate

**What is Framework?**

Framework is a collection of boilerplate projects for quick starting production-class 
python django based backend applications, particularly utilizing django as an ORM, 
and as an API server. Framework can help you built production-grade, secure, reliable
backend for your applications that scales, within minutes.

You would only need a fork!

**Variant: Minimum Config**

This variant of framework is a basic django project

### Features
* Setting secrets through environment variables
* Customizable, extensible User-Auth model

### How to Install?
1. Create a venv for python3, - `python3 -m venv ./venv`
2. Install dependencies, - `pip install -r requirements.txt`
3. Perform migrations - `python manage.py migrate`, if you dont have migration files 
already run `python manage.py makemigrations` to create migration files for your apps.
4. Create superuser (optional) - `python manage.py createsuper`
5. Run the application - `python manage.py runserver`

<hr>
Made with <3 by Ashwin Shenoy.