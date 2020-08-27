# Web_Based_List.

This is a project I took up while working as an intern at Mar&Mor Engineering services last year (2019), I worked as an electrical engineering 
intern. One day while talking with the head of the IT department, he told me about how it would be nice to have an online list of 
equipments and their prices, so everyone working in the firm could have access to them. So I decided to build one, even if it doesn't
get deployed it would be something fun to work on.

# AIM.
The aim of the project is to build an online list of equipments, specifications, and their prices so everyone working in the firm could have access. 
You would have to register as a user on the web platform to input anything, you could change the price of an equipment someone else uploaded assuming you are aware that price and specification of that equipment has changed and the person who initially uploaded it doesn't, of course it would be shown that you had made some changes. You could also change your password incase forgotten.

# Tools.
I used HTML, CSS and BOOTSTRAP for the front end.
I used the django web frame work for the backend.
In the case of deployment I created a postgres database. Although, while working on the site I used the sqlite that comes with django.


# How to view this project on your desktop.
Make sure you have pip installed on your system. If you have python 3.6 upwards, you would most likely have pip pre-installed. Have a virtual enviroment, if you do not have
virtual enviroment installed on your system you can install it using -> pip install virtualenv on your CLI. Once that is installed, proceed with the following steps:

- Clone the repo
- On your CLI, cd to the repo on your desktop.
- Create your own virtualenv -> virtualenv name_of_your_env
- Activate your env(windows) -> name_of_your_env\Scripts\activate 
   ''         ''   ''(ios)   -> source name_of_your_env/bin/activate
- Change directory to the applications root directory-> cd mar_mor
- Install the requirements-> pip install -r requirements.txt
- When this is done, activate the application -> python manage.py runserver
- Go to your web browser(I use Google chrome), create a new incognito page and type in http://127.0.0.1:8000

Kindly note: For this project I didn't add my secret key but you can generate your own secret key. Here are some websites that generate secret keys for django applications:
- https://djecrety.ir/
- https://miniwebtool.com/django-secret-key-generator/



# Slight drawback
The front end is not aesthetically pleasing, hence I am improving on my front-end skills by working on my html and css and also
adding javascript to the stack.



This project commenced a few months to the end of the year 2019 and
was completed two weeks into the year 2020.
