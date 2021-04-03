from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Student)
class UserAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'father_name','date_of_birth','address','city','state','pin_code','phone','email','class_opted','marks','date_enrolled' ]
    

