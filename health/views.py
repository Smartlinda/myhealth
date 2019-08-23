from django.shortcuts import render
from django.contrib.auth import authenticate,login
from .backends import EmailBackend
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.conf.urls import include
from .forms import CustomUserCreationForm
from .models import User
from django.shortcuts import redirect

#homepage after receptionist logs in
def recephome(request,id):
    context_dict = {}
    current_user = User.objects.get(id=id)
    context_dict['current'] = current_user
    response = render(request, 'health/recephome.html', context_dict)

    return response

#homepage after admin log in
def adminhome(request):
    context_dict = {}
    response = render(request, 'account/adminhome.html', context_dict)

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
    return redirect('login/')
# # If the request is a HTTP POST, try to pull out the relevant information.
#     if request.method == 'POST':
# # Gather the email and password provided by the user.
# # This information is obtained from the login form.
# # We use request.POST.get('<variable>') as opposed
# # to request.POST['<variable>'], because the
# # request.POST.get('<variable>') returns None if the
# # value does not exist, while request.POST['<variable>']
# # will raise a KeyError exception.
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#
# # Use Django's machinery to attempt to see if the username/password
# # combination is valid - a User object is returned if it is.
#         user = authenticate(username=email, password=password)
#
# # If we have a User object, the details are correct.
# # If None (Python's way of representing the absence of a value), no user
# # with matching credentials was found.
#         if user is not null:
#             # Is the account active? It could have been disabled.
#                 if user.is_active:
#                     # What is the role of the user? An admin or doctor?
#                     # Different roles will log into their own pages
#                     if user.user_type == 1:
# # If the account is valid and active, we can log the user in.
# # We'll send the user back to the homepage.
#                         login(request, user)
#                         return render(request, 'health/dochome.html', {})
#                     elif user.user_type == 2:
#                         login(request, user)
#                         return render(request, 'health/labhome.html', {})
#                     elif user.user_type == 3:
#                         login(request, user)
#                         return render(request, 'health/recephome.html', {})
#                     elif user.user_type == 4:
#                         login(request, user)
#                         return render(request, 'health/patienthome.html', {})
#                     elif user.user_type == 5:
#                         login(request, user)
#                         return render(request, 'health/adminhome.html', {})
#                 else:
# # An inactive account was used - no logging in!
#                     return HttpResponse("Your Rango account is disabled.")
#         else:
# # Bad login details were provided. So we can't log the user in.
#             print("Invalid login details: {0}, {1}".format(email, password))
#             return HttpResponse("Invalid login details supplied.")
# # The request is not a HTTP POST, so display the login form.
# # This scenario would most likely be a HTTP GET.
#     else:
# # No context variables to pass to the template system, hence the # blank dictionary object...
#         return render(request, 'health/login.html', {})

#FOR receptionist to see the schedule for the day
def recep_schedule(request):
    context_dict = {}
    user = request.user
    form = ScheduleForm
    context_dict['form'] = form
    try:
        appoints = Schedule.object.filter(date=datetime.date.today()).order_by('time')
        context_dict['appoints'] = appoints
    except Schedule.DoesNotExist:
        return redirect('recephome')

    return render(request,'health/recep_schedule.html',context_dict)

#FOR doctors to see the schedule for the day
def doc_schedule(request):
    context_dict = {}
    user = request.user
    form = ScheduleForm
    context_dict['form'] = form
    try:
        appoints_today = Schedule.object.filter(date=datetime.date.today()).filter(doctorid=user).order_by('time')
        context_dict['appoints'] = appoints_today
    except Schedule.DoesNotExist:
        return HttpResponse("No schedule for today.")

    return render(request,'health/doc_schedule.html',context_dict)

#for doctors to search the patient ???? maybe not necessary
# ??? since the doc can add notes through EHR->Schedule
def patient_result(request):
    mid = []
    query = request.GET.get('q')
    context_dict = {}
    if query:
        result = []
        k = [x.strip() for x in query.split()]
        for part in k:
            try:
                mid = User.objects.annotate(full_name=Concat('first_name', V(' '), 'last_name')).\
                filter(full_name__icontains=query).filter(user_type=4)
            except:
                mid = None
            if mid:
                result.append(mid)
        if len(result) == 0:
            result = None
        context_dict['result'] = result
    return ender(request,'health/patient_result.html',context_dict)

def search_patient(request):
    context_dict = {}
    return ender(request,'health/search_patient.html',context_dict)

#for doctors to view the EHR for accessing edit_schedule view
def doc_schedule_result(request,patient):
    context_dict = {}
    try:
        patient = User.objects.get(id=patient)
        context_dict['patient'] = patient
    except User.DoesNotExist:
        return redirect('search_patient')
    try:
        schedule = Schedule.objects.filter(patient=patient)
        context_dict['schedule'] = schedule
    except Schedule.DoesNotExist:
        return redirect('search_patient')

    return render(request,'health/doc_EHR.html',context_dict)

# def doc_edit_schEHR(request,schedule):
#     context_dict = {}
#     try:
#         schedule = Schedule.objects.get(id=schedule)
#         context_dict['schedule'] = schedule
#     except Schedule.DoesNotExist:
#         return redirect('doc_show_spePaSch', schedule.patient)

#for patients: all the schedules this patient has attended
def patient_show_schedule(request,nin):
    context_dict = {}
    user = request.user
    try:
        schedule = Schedule.objects.filter(patient=user)
        context_dict['schedule'] = schedule
    except Schedule.DoesNotExist:
        return HttpResponse("You don't have any appointment record with us.")

    return render(request,'health/patient_EHR.html',context_dict)

def patient_scheDetail(request,schedule):
    context_dict = {}
    return render(request,'health/pa_sche_detail.html',context_dict)

#for doctors to add notes, enter prescriptions etc.
def edit_schedule(request,scheduleID):
    context_dict = {}
    try:
        schedule = Schedule.objects.get(id=scheduleID)
        patient = schedule.patient
        context_dict['schedule'] = schedule
        context_dict['patient'] = patient
    except Schedule.DoesNotExist:
        return redirect('patient_show_EHR')
    form = ScheduleForm({'patient': patient, 'date':schedule.date, 'time':schedule.time, 'doctorid':schedule.doctorid, 'notes':schedule.notes})
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save(commit=True)
            return redirect('edit_schedule',schedule.id)
        else:
            print(form.errors)
    return render(request,'health/edit_schedule.html',context_dict)

#for doctors to request a specific test for a patient
def request_lab(request,schedule):
    context_dict = {}
    try:
        schedule = Schedule.objects.get(id=schedule)
    except Schedule.DoesNotExist:
        return redirect('edit_schedule',schedule.id)


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
    return redirect('/accounts/signup/')

#for patient to edit info stored in PHR
def edit_PHR(request):
    context_dict = {}
    return render(request,'health/edit_PHR.html',context_dict)

#for lab people to see what lab to do
def show_test(request):
    context_dict = {}
    return render(request,'health/show_test.html',context_dict)

#for patient to view test result
# def show_testR(request):
#     context_dict = {}
#     return render(request,'health/show_testR.html',context_dict)
