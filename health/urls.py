from django.urls import path,include
from health import views
from allauth.account.views import SignupView

urlpatterns = [
    path('',views.user_login,name='login'),
    path('login/doc/dochome/',views.dochome,name='dochome'),
    path('login/recep/recephome/', views.recephome, name='recephome'),
    path('login/lab/labhome/', views.labhome, name='labhome'),
    path('login/patient/patienthome/', views.patienthome, name='patienthome'),
    path('signup/doc/dochome/',views.dochome,name='dochome'),
    path('signup/recep/recephome/', views.recephome, name='recephome'),
    path('signup/lab/labhome/', views.labhome, name='labhome'),
    path('signup/patient/patienthome/', views.patienthome, name='patienthome'),
    path('doc/schedule/',views.doc_schedule,name='doc_schedule'),
    path('doc/search_patient/',views.search_patient,name='search_patient'),
    path('doc/patient_result/',views.patient_result,name='patient_result'),
    path('doc/pasche/<int:patient>/',views.doc_schedule_result,name='doc_schedule_result'),
    path('doc/edit_schedule/<int:scheduleID>/',views.edit_schedule,name='edit_schedule'),
    path('doc/request_lab/<int:schedule>/',views.request_lab,name='request_lab'),
    path('lab/test/', views.show_test, name='show_test'),
    path('lab/upload_result/<int:testID>/', views.upload_result, name='upload_result'),
    path('recep/book_appoint/', views.recep_book_appoint, name='recep_book'),
    path('recep/cancel_appoint/<int:scheduleID>/', views.recep_cancel_appoint, name='recep_cancel'),
    path('recep/schedule/', views.recep_schedule, name='recep_schedule'),
    path('patient/book_appoint/', views.patient_book_appoint, name='patient_book'),
    path('patient/cancel_appoint/<int:scheduleID>/', views.patient_cancel_appoint, name='patient_cancel'),
    path('patient/schedule/<int:nin>/', views.patient_show_schedule, name='patient_schedule'),
    path('patient/schedule_detail/<int:schedule>/', views.patient_scheDetail, name='patient_scheDetail'),
    path('patient/PHR/<int:nin>/', views.myPHR, name='myPHR'),

]
