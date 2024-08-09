from django.shortcuts import render
from consultation.models import *
import uuid, datetime


# https://chatgpt.com/c/ae6bf9ec-a3e0-48f1-9f7e-7521885594a0
def patient_id_generator(gender):
    gender = gender[0]
    return f'{gender}-'
print(patient_id_generator('Male'))

# Create your views here.
def home(request):
    departments = Department.objects.all()
    return render(request,'home.html',{'depts':departments})


def make_appointment(request,dslug):
    departments = Department.objects.get(slug=dslug)  
    if request.method == "POST":
        name_input = request.POST.get('name')
        gender_input = 'Male'
        email_input = request.POST.get('email')
        date_input = request.POST.get('date')
        time_input = request.POST.get('time')
        dept_input = request.POST.get('department')
        phone_input = request.POST.get('phone')
        message_input = request.POST.get('message')
        try:
            dept = Department.objects.get(name=dept_input).id
        except: 
            pass
        finally:
            new_patient = Patient.objects.create(name=name_input,patient_id='M199811',email=email_input,phone=phone_input)
            new_patient.save()

            new_appointment = Appointment.objects.create(patient=new_patient,date=date_input,department="oncology",
                                                 message=message_input,time=time_input)
            new_appointment.save()
    context = {'depts':departments}
    return render(request,'book appointment.html',context)

