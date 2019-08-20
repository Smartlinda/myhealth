# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.db.utils import IntegrityError
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    #use email as authentication
    username = None
    email = models.EmailField(_('email address'), unique=True)

    objects = CustomUserManager()
    # id = models.AutoField(primary_key=True)

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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type',]

    def __str__(self):
        return self.email
  # class Meta:
  #       db_table = 'auth_user'

class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,related_name='staff')
    # staff_id = models.IntegerField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE, db_column='department', blank=True, null=True)
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE, db_column='hospital', blank=True, null=True)
    # fname = models.CharField(max_length=255, blank=True, null=True)
    # lname = models.CharField(max_length=255, blank=True, null=True)
    # sex = models.BooleanField(blank=True, null=True)
    # tel_no = models.CharField(max_length=255, blank=True, null=True)
    # email = models.EmailField(max_length=255,unique=True)

    class Meta:
        db_table = 'Staff'

class Patient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='pat')
    nin = models.AutoField(db_column='NIN', primary_key=True)
    # email = models.EmailField(max_length=255,unique=True)
    # fname = models.CharField(max_length=255, blank=True, null=True)
    # lname = models.CharField(max_length=255, blank=True, null=True)
    # dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    # sex = models.BooleanField(blank=True, null=True)
    # tel_no = models.CharField(max_length=255,blank=True,null=True)
    # address = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        db_table = 'Patient'

class Department(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    hospitalid = models.ForeignKey('Hospital', on_delete=models.CASCADE, db_column='hospitalID')  # Field name made lowercase.
    tel_no = models.CharField(max_length=255)

    class Meta:
        db_table = 'Department'


class Disease(models.Model):
    name = models.CharField(max_length=255,primary_key=True)

    class Meta:
        db_table = 'Disease'


class Ehr(models.Model):
    schedule = models.ForeignKey('Schedule', db_column='schedule', primary_key=True, on_delete=models.CASCADE)
    medicalsupply = models.ManyToManyField('MedicalSupply')  # Field name made lowercase.
    amount = models.IntegerField()

    class Meta:
        db_table = 'EHR'

@receiver(m2m_changed, sender=Ehr.medicalsupply.through)
def verify_uniqueness(sender, **kwargs):
    ehr = kwargs.get('instance', None)
    action = kwargs.get('action', None)
    medicalsupply = kwargs.get('pk_set', None)

    if action == 'pre_add':
        for ms in medicalsupply:
            if Ehr.objects.filter(schedule=ehr.schedule).filter(medicalsupply=ms):
                raise IntegrityError('The same prescription has been issued in this appointment.')

class Hospital(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        db_table = 'Hospital'


class LabTest(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, db_column='patient')
    doctor = models.ForeignKey('Staff', on_delete=models.CASCADE, db_column='doctor',related_name='doc')
    name = models.CharField(max_length=255)
    conductor = models.OneToOneField('Staff', models.DO_NOTHING, db_column='conductor',related_name='conduct')
    report = models.FileField(upload_to='lab_report',blank=True)

    class Meta:
        db_table = 'Lab test'


class MedicalSupply(models.Model):
    name = models.CharField(max_length=255)
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    stock = models.IntegerField(default=0)

    class Meta:
        db_table = 'Medical supply'


class Order(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'Order'


class Orderdetail(models.Model):
    orderid = models.ForeignKey('Order', db_column='orderID', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    medicalsupply = models.ForeignKey('MedicalSupply', on_delete=models.CASCADE, db_column='medicalSupply')  # Field name made lowercase.
    amount = models.IntegerField()

    class Meta:
        db_table = 'OrderDetail'
        unique_together = (('orderid', 'medicalsupply'),)


class Phr(models.Model):
    patient = models.OneToOneField('Patient', db_column='patient', primary_key=True, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    doctorid = models.ForeignKey('Staff', on_delete=models.CASCADE, db_column='doctorID', blank=True, null=True)  # Field name made lowercase.
    disease = models.ForeignKey('Disease', on_delete=models.CASCADE, db_column='disease')

    class Meta:
        db_table = 'PHR'


class Schedule(models.Model):
    patient = models.OneToOneField('Patient', models.DO_NOTHING, db_column='patient')
    date_time = models.DateTimeField(db_column='date&time')  # Field renamed to remove unsuitable characters.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    notes = models.CharField(max_length=255,blank=True, null=True)
    waiting_time = models.TimeField(db_column='waiting time',blank=True,null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        db_table = 'Schedule'

# @receiver(post_save, sender=User)
# def create_s_or_p(sender, instance, created, **kwargs):
#     # Staff.objects.filter(email = 'xiong199704242@163.com').delete()
#     # Staff.objects.filter(email = 'xiong199704242@gmail.com').delete()
#     if instance.user_type in set([1,2,3,5]):
#         Staff.objects.get_or_create(user = instance)
#     else:
#         Patient.objects.get_or_create(user = instance)
#
# @receiver(post_save, sender=User)
# def save_sp_profile(sender, instance, **kwargs):
#     print('_-----')
#     if instance.user_type in set([1,2,3,5]):
#         instance.staff.save()
#     else:
#     # Patient.objects.get_or_create(user = instance,email=instance.email,fname=instance.first_name,lname=instance.last_name)
#         instance.pat.save()
