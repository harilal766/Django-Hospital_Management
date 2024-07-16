from django.shortcuts import render
from consultation.models import *

# Create your views here.
def home(request):
    departments = Department.objects.all()
    return render(request,'home.html',{'depts':departments})


def make_appointment(request):
    '''
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        department = request.POST['department']
        phone = request.POST['phone']
        message = request.POST['message']

        # Adding datas to respective tables and saving them
        patient = Patient.objects.create(name=name,email=email,phone=phone)
        patient.save()
        appointment = Appointment.objects.create(date=date,department=department,message=message)
        appointment.save()
    else:
        pass
    '''

    return render(request,'book appointment.html')
