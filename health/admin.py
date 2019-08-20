from django.contrib import admin
from health.models import User, Department, Staff, Disease, Ehr,Hospital,LabTest
from health.models import MedicalSupply,Order,Orderdetail,Phr,Patient,Schedule
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.utils.translation import ugettext_lazy as _


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active', 'first_name', 'last_name')
    list_filter = ('email', 'is_staff', 'is_active', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


# Register your models here.
admin.site.register(Staff)
admin.site.register(Patient)
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
