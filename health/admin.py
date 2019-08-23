from django.contrib import admin
from health.models import User, Department, Disease, Ehr,Hospital,LabTest
from health.models import MedicalSupply,Order,Orderdetail,Phr,Schedule
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.utils.translation import ugettext_lazy as _


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'first_name', 'last_name', 'user_type')



# Register your models here.
admin.site.register(User,CustomUserAdmin)
admin.site.register(Department)
admin.site.register(Disease)
admin.site.register(Ehr)
admin.site.register(Hospital)
admin.site.register(LabTest)
admin.site.register(MedicalSupply)
admin.site.register(Order)
admin.site.register(Orderdetail)
admin.site.register(Phr)
admin.site.register(Schedule)
