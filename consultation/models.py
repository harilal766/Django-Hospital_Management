from django.db import models

# Create your models here.
class Choices(models.Model):
    gender_choices = (
        ('M', 'Male'),
        ('F',"Female"),
        ('T','Transgender')
    )  


class Department(models.Model):
    name = name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=20)
    department = models.ForeignKey(Department,on_delete = models.CASCADE)
    joining_date = models.DateField()
    phone = models.CharField(max_length=12,default='1234')
    email = models.CharField(max_length=40,blank=True,default='exapmple@gmail.com')
    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='Patient/Photo',blank=True,null=True)
    gender = models.CharField(max_length=1, choices=Choices.gender_choices,default='Prefer Not to say')
    age = models.IntegerField(default=None,blank=True,null=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,blank=True,null=True)
    occupation = models.CharField(max_length=200,blank=True,null=True)
    address = models.CharField(max_length=1000,default = None,blank=True,null=True,unique=True)
    phone = models.CharField(max_length=14,default = '+91 12345678910',blank=True,null=True,unique=True)
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
    def __str__(self):
        return f'{self.patient.name} - {self.date}'
