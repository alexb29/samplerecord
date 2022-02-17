# samplerecord
Webapp to maintain a sample record written in django2.1
updatetd to Django==3.2.12

instruction to deploy in test mode:

download the zip and extract

create virtualenv using python 3.7 or above up to 3.10

Activate the virtualenv

In the requirement.txt folder:

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

if you want to have an user to deal only with the sample and not
with all the other aspects of the administration
create it in django admin and give him permissions to create and modify
samples.
