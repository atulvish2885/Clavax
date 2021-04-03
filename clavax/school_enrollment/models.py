from django.db import models

# Create your models here.
class Student(models.Model):
    class_choices= (('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'))
    student_name=models.CharField(max_length=50, blank = True, null = True,default = None )
    father_name=models.CharField(max_length=50, blank = True, null = True, default = None )
    date_of_birth =models.DateField()
    address=models.CharField(max_length=100,blank=True,null=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=25)
    pin_code=models.CharField(max_length=6,null=False)
    phone=models.CharField(max_length=10,unique=True)
    email=models.EmailField(max_length=50,unique=True)
    class_opted=models.CharField(choices=class_choices,max_length=10,blank=False)
    marks=models.CharField(max_length=100)
    date_enrolled=models.DateField()

    def __str__(self):
        return str(self.student_name,self.phone)



