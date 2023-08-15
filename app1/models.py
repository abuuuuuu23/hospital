from django.db import models


# Create your models here.
class tbl_patient(models.Model):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    date = models.DateField()
    gender = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

    class meta:
        db_patient = "tbl_patient"


class tbl_hospital(models.Model):
    id = models.IntegerField( primary_key=True)
    doctor_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=20)
    salary = models.IntegerField()
    experience = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)

    class meta:
        db_doctor = "tbl_hospital"
