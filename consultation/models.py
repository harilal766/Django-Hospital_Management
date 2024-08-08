from django.db import models

# Create your models here.
class Choice(models.Model):
    gender_choices = (
        ('M', 'Male'),
        ('F',"Female"),
        ('T','Transgender')
    )
class Status(models.Model):
    appoint_status = (
        ('Sc', 'Scheduled'),
        ('Co', 'Completed'),
        ('Ca', 'Cancelled')
    )



class Department(models.Model):
    name = name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Healthcare_professional(models.Model):
    name = models.CharField(max_length=20)
    joining_date = models.DateField()
    phone = models.CharField(max_length=12,default='1234')
    email = models.CharField(max_length=40,blank=True,default='exapmple@gmail.com')
    class Meta:
        abstract = True
    def __str__(self):
        return self.name


class Doctor(Healthcare_professional):
    department = models.ForeignKey(Department,on_delete = models.CASCADE,default='medicine')
    availability = models.DurationField(default=None)

class Nurse(Healthcare_professional):
    pass

class Pharmacist(Healthcare_professional):
    pass


class Patient(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='Patient/Photo',blank=True,null=True)
    gender = models.CharField(max_length=1, choices=Choice.gender_choices,default='Prefer Not to say')
    age = models.IntegerField(default=None,blank=True,null=True)
    patient_id = models.CharField(max_length=10,default=None)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,blank=True,null=True)
    occupation = models.CharField(max_length=200,blank=True,null=True)
    address = models.CharField(max_length=1000,default = None,blank=True,null=True,unique=True)
    phone = models.CharField(max_length=14,default = '+91 12345678910',blank=True,null=True)
    email = models.CharField(max_length=40,blank=True,default='exapmple@gmail.com')
    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,blank=True,null=True)
    date = models.DateField()
    time = models.TimeField(default='',blank=True,null=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,blank=True,null=True)
    message = models.TextField(max_length=1000,default='')
    status = models.CharField(max_length=2, choices=Status.appoint_status, null=True,)
    def __str__(self):
        return f'{self.patient.name} - {self.date}'