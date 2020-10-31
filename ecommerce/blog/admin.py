from django.contrib import admin

# Register your models here.
from .models import Blogpost,Blogcomment,Contactus
admin.site.register((Blogpost,Blogcomment,Contactus))