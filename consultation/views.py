from django.shortcuts import render
from consultation.models import *

# Create your views here.
def home(request):
    departments = Department.objects.all()
    return render(request,'home.html',{'depts':departments})


def make_appointment(request):
    departments = Department.objects.all()
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        department = request.POST.get('department')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # Adding datas to respective tables and saving them

        # add condition to make sure phone number is unique 
        new_patient = Patient.objects.create(name=name,email=email,phone=phone)
        new_patient.save()
        new_appointment = Appointment.objects.create(patient=new_patient,date=date,department=department,
                                                 message=message,time=time)
        new_appointment.save()
    return render(request,'book appointment.html',{'depts':departments})
