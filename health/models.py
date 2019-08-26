# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.db.utils import IntegrityError
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.validators import FileExtensionValidator


class User(AbstractUser):

    USER_TYPE_CHOICES = (
      (1, 'Doctor'),
      (2, 'Lab People'),
      (3, 'Receptionist'),
      (4, 'Patient'),
      (5, 'Administration'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,null=True)
    sex = models.BooleanField(blank=True, null=True)
    tel_no = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(db_column='DOB', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    # USERNAME_FIELD = 'email'
    # EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type','email','password',]

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return "/health/%i/" % (self.pk)


class Department(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE, db_column='hospital',blank=True, null=True)  # Field name made lowercase.
    tel_no = models.CharField(max_length=255)

    class Meta:
        db_table = 'Department'


class Disease(models.Model):
    name = models.CharField(max_length=255,primary_key=True)

    class Meta:
        db_table = 'Disease'

    @classmethod
    def create(cls, name):
        dis = cls(name=name)
        # do something with the book
        return dis


class Ehr(models.Model):
    schedule = models.ForeignKey('Schedule', db_column='schedule', on_delete=models.CASCADE)
    medicalsupply = models.ForeignKey('MedicalSupply',on_delete=models.CASCADE,null=True,blank=True)  # Field name made lowercase.
    amount = models.IntegerField(default=0,null=True,blank=True)

    class Meta:
        db_table = 'EHR'
        unique_together = (('schedule', 'medicalsupply'),)

    @classmethod
    def create(cls, schedule,medicalsupply,amount):
        ehr = cls(schedule=schedule,medicalsupply=medicalsupply,amount=amount)
        # do something with the book
        return ehr


class Hospital(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255,unique=True)
    address = models.CharField(max_length=255)

    class Meta:
        db_table = 'Hospital'

    @classmethod
    def create(cls, name,address):
        hospital = cls(name=name,address=address)
        # do something with the book
        return hospital


class LabTest(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    done = models.BooleanField(default=False)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='patient')
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='doctor',related_name='doc')
    name = models.CharField(max_length=255,null=True,blank=True)
    conductor = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='conductor',related_name='conduct',null=True,blank=True)
    report = models.FileField(upload_to='report/',validators=[FileExtensionValidator(allowed_extensions=['pdf'])],null=True,blank=True)

    class Meta:
        db_table = 'Lab test'


class MedicalSupply(models.Model):
    name = models.CharField(max_length=255)
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    stock = models.IntegerField(default=0)

    class Meta:
        db_table = 'Medical supply'

    @classmethod
    def create(cls, name,stock):
        ms = cls(name=name,stock=stock)
        # do something with the book
        return ms


class Order(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    datetime = models.DateTimeField(default = timezone.now)

    class Meta:
        db_table = 'Order'

    @classmethod
    def create(cls, datetime):
        order = cls(datetime=datetime)
        # do something with the book
        return order


class Orderdetail(models.Model):
    orderid = models.ForeignKey('Order', db_column='orderID', on_delete=models.CASCADE)  # Field name made lowercase.
    medicalsupply = models.ForeignKey('MedicalSupply', on_delete=models.CASCADE, db_column='medicalSupply')  # Field name made lowercase.
    amount = models.IntegerField()

    class Meta:
        db_table = 'OrderDetail'
        unique_together = (('orderid', 'medicalsupply'),)


class Phr(models.Model):
    patient = models.OneToOneField(settings.AUTH_USER_MODEL, db_column='patient', primary_key=True, on_delete=models.CASCADE,related_name='phr_pat')
    weight = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    doctorid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='doctorID', blank=True, null=True,related_name='phr_doc')  # Field name made lowercase.
    disease = models.ForeignKey('Disease', on_delete=models.CASCADE, db_column='disease', blank=True, null=True)

    class Meta:
        db_table = 'PHR'


class Schedule(models.Model):
    checked_in = models.BooleanField(default=False)  #whether the patient has checked in or not
    booked = models.BooleanField(default=False)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='patient',blank=True,null=True,related_name='sche_pat')
    date = models.DateField(blank=True,null=True)  # Field renamed to remove unsuitable characters.
    time = models.TimeField(blank=True,null=True)
    doctorid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='doctorID', blank=True, null=True,related_name='sche_doc')
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sysmptoms = models.TextField(max_length=65535,blank=True, null=True)
    diagnosis = models.TextField(max_length=65535,blank=True, null=True)
    prescriptions = models.TextField(max_length=65535,blank=True, null=True)
    treatment = models.TextField(max_length=65535,blank=True, null=True)
    waiting_time = models.TimeField(db_column='waiting time',blank=True,null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        db_table = 'Schedule'

    @classmethod
    def create(cls, checked_in,patient,date,time,doctorid):
        schedule = cls(checked_in=checked_in,patient=patient,date=date,time=time,doctorid=doctorid)
        # do something with the book
        return schedule
