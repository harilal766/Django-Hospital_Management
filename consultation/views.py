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
        department = request.POST.get('department')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Adding datas to respective tables and saving them
        patient = Patient.objects.create(name=name,email=email,phone=phone)
        patient.save()
        appointment = Appointment.objects.create(date=date,department=department,message=message)
        appointment.save()
    else:
        pass
    

    return render(request,'book appointment.html',{'depts':departments})
