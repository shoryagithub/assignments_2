===============================================================
          Adding Model Objects Using Django Admin
===============================================================

There are few step and to add a Model Object and Django Admin.

STEP-1 First we have to define a model (models.py)

the simple format for defining the model 
from django.db import models


class ModelName(models.Model):
    field_name_1 = models.FieldType(arguments)
    field_name_2 = models.FieldType(arguments)
    ...
    
    def __str__(self):
        return self.field_name_1 


there are many field types in Django like ,
CharField
IntegerField
TextField
EmailField
DateField
BooleanField
FloatField
FileField
ImageField
and many more.

Step 2: then Register the Model in (admin.py)   

the simple format to register a model 

from django.contrib import admin
from .models import YourModelName

admin.site.register(YourModelName)

YourModelName - this means the name of your model that you ave created.

After register we create a super user in step 3

Step 3: Creating a Superuser

A superuser is the main admin of a Django project
 Why Do We Create a Superuser?
We create it to:
Use the admin dashboard to manage our models easily.
Add or update data without writing any code.
Test if the admin panel is working or not.
Create other users or staff if needed.

We create superuser with the command 

" python manage.py createsuperuser "

Then Django will ask:

What’s your username?
What’s your email? 
What’s your password?

then start the server with the command 
  " python manage.py runserver "

then open your brower and go to: 
  "http://127.0.0.1:8000/admin/"

  and the login with the username and pssword that you ahev create.