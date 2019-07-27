# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser, User

class User(AbstractUser):
  USER_TYPE_CHOICES = (
      (1, 'doctor'),
      (2, 'labPeople'),
      (3, 'receptionist'),
      (4, 'patient'),
      (5, 'admin'),
  )

  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,null=True)
  # class Meta:
  #       db_table = 'auth_user'

class Department(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    hospitalid = models.ForeignKey('Hospital', models.DO_NOTHING, db_column='hospitalID')  # Field name made lowercase.
    tel_no = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Department'


class Disease(models.Model):
    name = models.CharField(max_length=255,primary_key=True)

    class Meta:
        managed = False
        db_table = 'Disease'


class Ehr(models.Model):
    schedule = models.OneToOneField('Schedule', db_column='schedule', primary_key=True, on_delete=models.CASCADE)
    medicalsupply = models.ForeignKey('MedicalSupply', models.DO_NOTHING, db_column='medicalSupply')  # Field name made lowercase.
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'EHR'
        unique_together = (('schedule', 'medicalsupply'),)


class Hospital(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Hospital'


class LabTest(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    patient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patient')
    doctor = models.ForeignKey('Staff', models.DO_NOTHING, db_column='doctor',related_name='doc')
    name = models.CharField(max_length=255)
    conductor = models.ForeignKey('Staff', models.DO_NOTHING, db_column='conductor',related_name='conduct')
    report = models.TextField()

    class Meta:
        managed = False
        db_table = 'Lab test'


class MedicalSupply(models.Model):
    name = models.CharField(max_length=255)
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Medical supply'


class Order(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Order'


class Orderdetail(models.Model):
    orderid = models.OneToOneField(Order, db_column='orderID', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    medicalsupply = models.ForeignKey(MedicalSupply, models.DO_NOTHING, db_column='medicalSupply')  # Field name made lowercase.
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'OrderDetail'
        unique_together = (('orderid', 'medicalsupply'),)


class Phr(models.Model):
    patient = models.OneToOneField('Patient', db_column='patient', primary_key=True, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    doctorid = models.ForeignKey('Staff', models.DO_NOTHING, db_column='doctorID', blank=True, null=True)  # Field name made lowercase.
    disease = models.ForeignKey(Disease, models.DO_NOTHING, db_column='disease')

    class Meta:
        managed = False
        db_table = 'PHR'


class Patient(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    sex = models.BooleanField(blank=True, null=True)
    tel_no = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    nin = models.IntegerField(db_column='NIN', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Patient'


class Schedule(models.Model):
    patient = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patient')
    date_time = models.DateTimeField(db_column='date&time')  # Field renamed to remove unsuitable characters.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    notes = models.CharField(max_length=255,blank=True, null=True)
    waiting_time = models.TimeField(db_column='waiting time')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Schedule'


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    tel_no = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department', blank=True, null=True)
    hospital = models.ForeignKey(Hospital, models.DO_NOTHING, db_column='hospital', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Staff'
