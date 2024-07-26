from django.shortcuts import render
from consultation.models import Appointment,Doctor,Nurse,Pharmacist
# Create your views here.
def dashboard(request):
    # Number of healthcare professionals present on a working day
    doctors = Doctor.objects.all().count
    nurses = Nurse.objects.all().count
    pharmacists = Pharmacist.objects.all().count

    appoint = Appointment.objects.all()

    context = {
        'doctors':doctors,
        'nurses':nurses,
        'pharmacists':pharmacists,
        'appoint':appoint
        }
    return render(request,"dashboard.html",context)