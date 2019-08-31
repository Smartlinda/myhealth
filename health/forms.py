from django import forms
from health.models import User, Department, Disease, Ehr,Hospital,LabTest
from health.models import MedicalSupply,Order,Orderdetail,Phr,Schedule
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from health.widgets import SelectTimeWidget
from datetimewidget.widgets import DateWidget,TimeWidget

class CustomUserCreationForm(UserCreationForm):

    tel_no = forms.CharField(max_length=255, label='Telephone number')
    dob = forms.DateField(label='Date of Birth',input_formats=['%Y/%m/%d'],help_text='YYYY/mm/dd')
    SEX = [('yes','Female'),('no','Male')]
    sex = forms.BooleanField(label='Sex',widget=forms.Select(choices = SEX))


    class Meta(UserCreationForm):
        model = User
        fields = ('email','user_type','first_name','last_name','sex','tel_no','dob','address','password',)

    # def __init__(self,user,*args,**kwargs):



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email','user_type','first_name','last_name','sex','tel_no','dob','address',)


class SignupForm(forms.ModelForm):
    tel_no = forms.CharField(max_length=255, label='Telephone number')
    dob = forms.DateField(label='Date of Birth', input_formats=['%Y-%m-%d'],help_text='YYYY-mm-dd')
    SEX = [('yes','Female'),('no','Male')]
    sex = forms.BooleanField(label='Sex',widget=forms.Select(choices = SEX))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.user_type = self.cleaned_data['user_type']
        user.sex = self.cleaned_data['sex']
        user.tel_no = self.cleaned_data['tel_no']
        user.dob = self.cleaned_data['dob']
        user.address = self.cleaned_data['address']
        user.save()

    class Meta:
        model = User
        fields = ('email','user_type','first_name','last_name','sex','tel_no','dob','address',)

class NoteForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('sysmptoms','treatment','prescriptions','diagnosis',)


class DepartmentForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    tel_no = forms.CharField(max_length=255)
    class Meta:
        model = Department
        exclude = ('hospital',)

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
    report = forms.FileField(required=False)
    conductor = forms.ModelChoiceField(queryset=get_user_model().objects,required=False)
    class Meta:
        model = LabTest
        exclude = ('id','done',)

class ReportForm(forms.ModelForm):

    class Meta:
        model = LabTest
        fields = ('report',)

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
        exclude = ('doctorid','disease','patient',)

# class PatientForm(forms.ModelForm):
#     class Meta:
#         model = Patient
#         exclude = ('user',)

class ScheduleForm(forms.ModelForm):
    # date = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'])
    date = forms.DateField(input_formats=['%d/%m/%Y'])
    time = forms.TimeField(widget=SelectTimeWidget(minute_step=15))
    doctorid = forms.ModelChoiceField(label = 'Doctor',queryset=get_user_model().objects,required=False)
    class Meta:
        model = Schedule
        fields = ('patient','time','doctorid','date',)
