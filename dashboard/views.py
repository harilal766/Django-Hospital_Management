from django.shortcuts import render
from consultation.models import Appointment,Doctor,Nurse,Pharmacist,Patient
# Create your views here.
site_name = 'Health Center'
def dashboard(request):
    # Number of healthcare professionals present on a working day
    doctors = Doctor.objects.all().count
    nurses = Nurse.objects.all().count
    pharmacists = Pharmacist.objects.all().count
    patients = Patient.objects.all().count

    appoint = Appointment.objects.all()

    context = {
        'doctors':doctors,
        'nurses':nurses,
        'pharmacists':pharmacists,
        'patients':patients,
        'appoint':appoint,
        'name' :site_name
        }
    return render(request,"dashboard.html",context)