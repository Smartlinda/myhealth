from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.conf.urls import include
from health.models import Staff
from .forms import CustomUserCreationForm

#homepage after receptionist logs in
def recephome(request):
    context_dict = {}
    current_user = request.user
    context_dict['current'] = current_user
    response = render(request, 'health/recephome.html', context_dict)

    return response

#homepage after admin log in
def adminhome(request):
    context_dict = {}
    response = render(request, 'health/adminhome.html', context_dict)

    return response

#homepage after doctor log in
def dochome(request):
    context_dict = {}
    response = render(request, 'health/dochome.html', context_dict)

    return response

#homepage after lab person log in
def labhome(request):
    context_dict = {}
    response = render(request, 'health/labhome.html', context_dict)

    return response

#homepage after patient log in
def patienthome(request):
    context_dict = {}
    response = render(request, 'health/patienthome.html', context_dict)

    return response

#view for authentication
def user_login(request):
# If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
# Gather the email and password provided by the user.
# This information is obtained from the login form.
# We use request.POST.get('<variable>') as opposed
# to request.POST['<variable>'], because the
# request.POST.get('<variable>') returns None if the
# value does not exist, while request.POST['<variable>']
# will raise a KeyError exception.
        email = request.POST.get('email')
        password = request.POST.get('password')

# Use Django's machinery to attempt to see if the username/password
# combination is valid - a User object is returned if it is.
        user = authenticate(email=email, password=password)

# If we have a User object, the details are correct.
# If None (Python's way of representing the absence of a value), no user
# with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
                if user.is_active:
                    # What is the role of the user? An admin or doctor?
                    # Different roles will log into their own pages
                    if user.user_type == 1:
# If the account is valid and active, we can log the user in.
# We'll send the user back to the homepage.
                        login(request, user)
                        return render(request, 'health/dochome.html', {})
                    elif user.user_type == 2:
                        login(request, user)
                        return render(request, 'health/labhome.html', {})
                    elif user.user_type == 3:
                        login(request, user)
                        return render(request, 'health/recephome.html', {})
                    elif user.user_type == 4:
                        login(request, user)
                        return render(request, 'health/patienthome.html', {})
                    elif user.user_type == 5:
                        login(request, user)
                        return render(request, 'health/adminhome.html', {})
                else:
# An inactive account was used - no logging in!
                    return HttpResponse("Your Rango account is disabled.")
        else:
# Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
# The request is not a HTTP POST, so display the login form.
# This scenario would most likely be a HTTP GET.
    else:
# No context variables to pass to the template system, hence the # blank dictionary object...
        return render(request, 'health/login.html', {})

#FOR receptionist to see the schedule for the day
def recep_schedule(request):
    context_dict = {}
    return render(request,'health/recep_schedule.html',context_dict)

#FOR doctors to see the schedule for the day
def doc_schedule(request):
    context_dict = {}
    return render(request,'health/doc_schedule.html',context_dict)

#for doctors to search the patient ???? maybe not necessary
# ??? since the doc can add notes through EHR->Schedule
def search_patient(request):
    context_dict = {}
    return ender(request,'health/search_patient.html',context_dict = {})

#for doctors to view the EHR for accessing edit_schedule view
def doc_show_EHR(request,nin):
    context_dict = {}
    return render(request,'health/doc_EHR.html',context_dict)

#for patients to view the EHR for accessing edit_schedule view
def patient_show_EHR(request,nin):
    context_dict = {}
    return render(request,'health/patient_EHR.html',context_dict)

#for doctors to add notes, enter prescriptions etc.
def edit_schedule(request,scheduleID):
    context_dict = {}
    return render(request,'health/edit_schedule.html',context_dict)

#for doctors to request a specific test for a patient
def request_lab(request):
    context_dict = {}
    return render(request,'health/request_lab.html',context_dict)

#for lab people to upload report of the test
def upload_result(request,testID):
    context_dict = {}
    return render(request,'health/upload_result.html',context_dict)

#for receptionist to book appointments
def recep_book_appoint(request):
    context_dict = {}
    return render(request,'health/recep_book_appoint.html',context_dict)

#for patients to book appointments
def patient_book_appoint(request):
    context_dict = {}
    return render(request,'health/patient_book_appoint.html',context_dict)

#for receptionist to cancel appointments
def recep_cancel_appoint(request):
    context_dict = {}
    return render(request,'health/recep_cancel_appoint.html',context_dict)

#for patients to cancel appointments
def patient_cancel_appoint(request):
    context_dict = {}
    return render(request,'health/patient_cancel_appoint.html',context_dict)


#for admin to check the stock of all medical supplies
# def view_stock(request):
#     context_dict = {}
#     return render(request,'health/view_stock.html',context_dict)

#for admin to create an account for patients and staffs
def create_account(request):
    context_dict = {}
    form = CustomUserCreationForm
    context_dict['form'] = form
    return render(request,'health/create_account.html',context_dict)

#for patient to edit info stored in EHR
def edit_EHR(request):
    context_dict = {}
    return render(request,'health/edit_EHR.html',context_dict)

#for lab people to see what lab to do
def show_test(request):
    context_dict = {}
    return render(request,'health/show_test.html',context_dict)

#for patient to view test result
# def show_testR(request):
#     context_dict = {}
#     return render(request,'health/show_testR.html',context_dict)
