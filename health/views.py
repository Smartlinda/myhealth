from django.shortcuts import render
from django.contrib.auth import authenticate,login
from .backends import EmailBackend
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.conf.urls import include
from health.forms import CustomUserCreationForm,CustomUserChangeForm,SignupForm,NoteForm
from health.forms import DepartmentForm,DiseaseForm,EhrForm,HospitalForm,LabTestForm,ReportForm
from health.forms import MedicalSupplyForm,OrderForm,OrderdetailForm,PhrForm,ScheduleForm
from django.shortcuts import redirect
from health.models import User, Department, Disease, Ehr,Hospital,LabTest
from health.models import MedicalSupply,Order,Orderdetail,Phr,Schedule
import datetime
from django.db.models import Q
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from time import sleep
from django.db import IntegrityError, transaction

#homepage after receptionist logs in
@login_required
def recephome(request):
    context_dict = {}
    user = request.user
    context_dict['current'] = user
    response = render(request, 'health/recephome.html', context_dict)

    return response


#homepage after doctor log in
@login_required
def dochome(request):
    context_dict = {}
    context_dict['current'] = request.user
    response = render(request, 'health/dochome.html', context_dict)

    return response

#homepage after lab person log in
@login_required
def labhome(request):
    context_dict = {}
    context_dict['current'] = request.user
    response = render(request, 'health/labhome.html', context_dict)

    return response

#homepage after patient log in
@login_required
def patienthome(request):
    context_dict = {}
    context_dict['current'] = request.user
    response = render(request, 'health/patienthome.html', context_dict)

    return response

#view for authentication
def user_login(request):
    return redirect('login/')

# class SignUp(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('adminhome')
#     template_name = 'signup.html'

#FOR doctors to see the schedule for the day
@login_required
def doc_schedule(request):
    context_dict = {}
    user = request.user
    context_dict['current'] = user
    try:
        appoints_today = Schedule.objects.filter(doctorid=user).order_by('time')
        context_dict['appoints'] = appoints_today
    except Schedule.DoesNotExist:
        return HttpResponse("No schedule for today.")

    return render(request,'health/doc_schedule.html',context_dict)

# search result of patient by doctor
@login_required
def patient_result(request):
    patient_list = User.objects.filter(user_type=4)
    query = request.GET.get('q')
    context_dict = {}
    context_dict['current'] = request.user
    if query:
        for term in query.split():
            patient_list = patient_list.filter( Q(first_name__icontains = term) | Q(last_name__icontains = term))
        context_dict['result'] = patient_list
    return render(request,'health/patient_result.html',context_dict)

#for doctors to search the patient
@login_required
def search_patient(request):
    context_dict = {}
    context_dict['current'] = request.user
    return render(request,'health/search_patient.html',context_dict)

#for doctors to view all the schedules related to that patient
@login_required
def doc_schedule_result(request,patient):
    context_dict = {}
    context_dict['current'] = request.user
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

#FOR receptionist to see the schedule for the day
@login_required
def recep_schedule(request):
    context_dict = {}
    user = request.user
    context_dict['current'] = user
    try:
        appoints = Schedule.objects.exclude(patient=None).order_by('date','time')
        context_dict['appoints'] = appoints
    except Schedule.DoesNotExist:
        return redirect('recephome')

    return render(request,'health/recep_schedule.html',context_dict)


# for the patient to see all the appointments they booked
@login_required
def patient_show_schedule(request,nin):
    context_dict = {}
    user = request.user
    context_dict['current'] = user
    try:
        schedule = Schedule.objects.filter(patient=user)
        context_dict['appoints'] = schedule
    except Schedule.DoesNotExist:
        return HttpResponse("You don't have any appointment record with us.")

    return render(request,'health/patient_schedule.html',context_dict)

#for the patient to view the notes left by the doctor
@login_required
def patient_scheDetail(request,schedule):
    context_dict = {}
    user = request.user
    context_dict['current'] = user
    schedule = Schedule.objects.get(id=schedule)
    context_dict['schedule'] = schedule
    return render(request,'health/pa_sche_detail.html',context_dict)

#for patient to view his own body related index such as weight and height
#patient can update the data as well
@login_required
def myPHR(request,nin):
    context_dict = {}
    user = request.user
    context_dict['current'] = user
    labs = LabTest.objects.filter(patient=user)
    context_dict['lab'] = labs
    schedules = Schedule.objects.filter(patient=user)
    context_dict['schedules'] = schedules
    phr = Phr.objects.get_or_create(patient=user)[0]
    context_dict['phr'] = phr
    form = PhrForm({'patient':user})
    if request.method == 'POST':
        form = PhrForm(request.POST, instance=phr)
        if form.is_valid():
            form.save(commit=True)
            return redirect('myPHR',user.id)
        else:
            print(form.errors)

    context_dict['form'] = form
    return render(request,'health/myPHR.html',context_dict)

#for doctors to add notes, enter prescriptions etc.
@login_required
def edit_schedule(request,scheduleID):
    context_dict = {}
    context_dict['current'] = request.user
    try:
        schedule = Schedule.objects.get(id=scheduleID)
        patient = schedule.patient
        lab_test = LabTest.objects.filter(patient=patient).exclude(name=None)
        context_dict['lab'] = lab_test
        context_dict['schedule'] = schedule
        context_dict['patient'] = patient
    except Schedule.DoesNotExist:
        return redirect('doc_schedule_result', patient)
    noteform = NoteForm()
    if request.method == 'POST':
        noteform = NoteForm(request.POST, instance=schedule)
        if noteform.is_valid():
            noteform.notes = request.POST
            noteform.save()
            return redirect('edit_schedule',schedule.id)
        else:
            noteform = NoteForm(request.GET or None)
            print(noteform.errors)
    context_dict['form'] = noteform
    return render(request,'health/edit_schedule.html',context_dict)

#for doctors to request a specific test for a patient
@login_required
def request_lab(request,schedule):
    context_dict = {}
    user = request.user
    context_dict['current'] = user

    try:
        schedule = Schedule.objects.get(id=schedule)
        patient = schedule.patient
        context_dict['schedule'] = schedule
        context_dict['patient'] = patient
    except Schedule.DoesNotExist:
        return redirect('edit_schedule',schedule.id)
    lab = LabTest.objects.get_or_create(patient=patient,doctor=user,done=False)[0]
    context_dict['lab'] = lab
    lab_form = LabTestForm({'patient':patient, 'doctor':user})
    if request.method == 'POST':
        lab_form = LabTestForm(request.POST, instance=lab)
        if lab_form.is_valid():
            lab_form.save(commit=True)

            return redirect('edit_schedule', schedule.id)
        else:
            print(lab_form.errors)

    context_dict['form'] = lab_form

    return render(request,'health/request_lab.html',context_dict)

#for lab people to upload report of the test
@login_required
def upload_result(request,testID):
    context_dict = {}
    user = request.user
    context_dict['current'] = user
    test = LabTest.objects.get(id=testID)
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES, instance=test)
        if form.is_valid():
            test.report = request.FILES['report']
            test.done = True
            test.conductor = user
            form.save()
            return redirect('show_test')
        else:
            form = ReportForm(request.GET or None)
            print(form.errors)
    context_dict['form'] = form
    return render(request,'health/upload_result.html',context_dict)

#for receptionist to book appointments
@login_required
def recep_book_appoint(request):
    context_dict = {}
    context_dict['current'] = request.user
    all_docs = User.objects.filter(user_type=1)
    schedule = Schedule.objects.create()
    form = ScheduleForm()
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save(commit=True)

            return redirect('recephome')
        else:
            print(form.errors)

    context_dict['form'] = form

    return render(request,'health/recep_book_appoint.html',context_dict)

#for patients to book appointments
@login_required
def patient_book_appoint(request):
    context_dict = {}
    user = request.user
    context_dict['current'] = user
    all_docs = User.objects.filter(user_type=1)
    schedule = Schedule.objects.create()
    form = ScheduleForm({'patient':user})
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save(commit=True)

            return redirect('patienthome')
        else:
            print(form.errors)

    context_dict['form'] = form

    return render(request,'health/patient_book_appoint.html',context_dict)

#for receptionist to cancel appointments
@login_required
def recep_cancel_appoint(request,scheduleID):
    context_dict = {}
    user = request.user
    able = False
    context_dict['current'] = user
    try:
        schedule = Schedule.objects.get(id=scheduleID)
        context_dict['schedule'] = schedule
    except Schedule.DoesNotExist:
        return redirect('recep_schedule')
    try:
        schedule.delete()
        return redirect('recep_schedule')
    except:
        pass
    return render(request,'health/recep_schedule.html',context_dict)

#for patients to cancel appointments
@login_required
def patient_cancel_appoint(request,scheduleID):
    context_dict = {}
    user = request.user
    context_dict['current'] = user
    able = False
    try:
        schedule = Schedule.objects.get(id=scheduleID)
        context_dict['schedule'] = schedule
    except Schedule.DoesNotExist:
        return redirect('patient_show_schedule', user.id)
    try:
        schedule.delete()
        return redirect('patient_show_schedule', user.id)
    except:
        pass


    return render(request,'health/patient_schedule.html',context_dict)

#for lab people to see what lab to do
@login_required
def show_test(request):
    context_dict = {}
    user = request.user
    context_dict['current'] = user
    try:
        test_list = LabTest.objects.filter(done=False)
        context_dict['tests'] = test_list
    except LabTest.DoesNotExist:
        return HttpResponse("No tests to do.")
    return render(request,'health/show_test.html',context_dict)

#for patient to view test result
# def show_testR(request):
#     context_dict = {}
#     return render(request,'health/show_testR.html',context_dict)
