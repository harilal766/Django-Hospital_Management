from django.shortcuts import render
from consultation.models import Appointment
# Create your views here.
def dashboard(request):
    appoint = Appointment.objects.all()

    context = {'appoint':appoint}
    return render(request,"dashboard.html",context)