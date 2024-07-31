## This file describes step by step how you can run easy drive app locaaly
## Use the app locally....

Make sure you have python installed on your OS
Clone the app
cd in the app
## Create a virtual environment
python -m venv venv
activate the virtual environment
source venv/Scripts/activate
## !(make sure you are in gitbash)
install packages
pip install django
pip install pillow
(pillow is a package that deals with images and files)
running the app
python manage.py runserver
