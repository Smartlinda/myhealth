from django import forms
from health.models import User, Department, Staff, Disease, Ehr,Hospital,LabTest
from health.models import MedicalSupply,Order,Orderdetail,Phr,Patient,Schedule
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email','user_type',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email','user_type',)


class StaffForm(forms.ModelForm):
    fname = forms.CharField(max_length=255)
    lname = forms.CharField(max_length=255)
    tel_no = forms.CharField(max_length=255)
    sex = forms.BooleanField()
    email = forms.EmailField(max_length=255)
    class Meta:
        model = Staff
        exclude = ('user','id','department','hospital',)

class DepartmentForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    tel_no = forms.CharField(max_length=255)
    class Meta:
        model = Department
        exclude = ('hospitalid',)

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ('name',)

class EhrForm(forms.ModelForm):
    amount = forms.IntegerField()
    class Meta:
        model = Ehr
        exclude = ('medicalsupply',)
        unique_together = (('schedule', 'medicalsupply'),)

class HospitalForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    class Meta:
        model = Hospital
        fields = ('id','name','address',)

class LabTestForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    report = forms.FileField()
    class Meta:
        model = LabTest
        exclude = ('patient','doctor','conductor',)

class MedicalSupplyForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    stock = forms.IntegerField()
    class Meta:
        model = MedicalSupply
        fields = ('id','name','stock',)

class OrderForm(forms.ModelForm):
    datetime = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'])
    class Meta:
        model = Order
        fields = ('id','datetime',)

class OrderdetailForm(forms.ModelForm):
    class Meta:
        model = Orderdetail
        exclude = ('medicalsupply',)
        unique_together = (('orderid', 'medicalsupply'),)

class PhrForm(forms.ModelForm):
    class Meta:
        model = Phr
        exclude = ('doctorid','disease',)

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ('user',)

class ScheduleForm(forms.ModelForm):
    date_time = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'])
    class Meta:
        model = Schedule
        exclude = ('patient',)
