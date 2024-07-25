from django.shortcuts import render
from consultation.models import *

# Create your views here.
def home(request):
    departments = Department.objects.all()
    return render(request,'home.html',{'depts':departments})


def make_appointment(request):
    departments = Department.objects.all()  
    if request.method == "POST":
        name_input = request.POST.get('name')
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
            new_patient = Patient.objects.create(name=name_input,email=email_input,phone=phone_input)
            new_patient.save()

            new_appointment = Appointment.objects.create(patient=new_patient,date=date_input,department=dept,
                                                 message=message_input,time=time_input)
            new_appointment.save()
    context = {'depts':departments}
        
    #return render(request_input,'home.html'_input,{'depts':departments})
    return render(request,'book appointment.html',context)
