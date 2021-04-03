from django.shortcuts import render
from .forms import UserForm
from . serializers import *
from rest_framework import viewsets

# Create your views here.

# def home(request):
#    return render(request,'home.html')

def homepage(request):
    form=UserForm()
    return render(request,'homepage.html',{'form':form})

def renderpage(request):
   # phone = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      form = UserForm(request.POST or None)
      
      if form.is_valid():
        print('form is valid')
        
        student_name = form.cleaned_data['student_name']
        father_name = form.cleaned_data['father_name']
        date_of_birth = form.cleaned_data['date_of_birth']
        address = form.cleaned_data['address']
        city = form.cleaned_data['city']
        state = form.cleaned_data['state']
        pin_code = form.cleaned_data['pin_code']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        class_opted = form.cleaned_data['class_opted']
        marks = form.cleaned_data['marks']
        date_enrolled = form.cleaned_data['date_enrolled']



        

        print("Form Valid")
        form.save()
         
   else:
      form = UserForm()
		
   return render(request, 'renderpage.html', {"student_name" : student_name,"father_name":father_name,"date_of_birth": date_of_birth,"address":address,"city":city,
   "state":state,"pin_code":pin_code,"phone":phone,"email":email,"class_opted":class_opted,"marks":marks,"date_enrolled":date_enrolled})
class Studentlist(viewsets.ModelViewSet):

   serializer_class = StudentListSerializer
   queryset = Student.objects.all()