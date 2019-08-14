from django.urls import path,include
from health import views

urlpatterns = [
    path('',views.user_login,name='login'),
    path('doc/dochome/',views.dochome,name='dochome'),
    path('recep/recephome/', views.recephome, name='recephome'),
    path('lab/labhome/', views.labhome, name='labhome'),
    path('admin/adminhome/', views.adminhome, name='adminhome'),
    path('patient/patienthome/', views.patienthome, name='patienthome'),
    path('doc/schedule/',views.schedule,name='doc_schedule'),
    path('doc/search_patient/',views.search_patient,name='search_patient'),
    path('doc/EHR/<int:nin>/',views.show_EHR,name='doc_EHR'),
    path('doc/edit_schedule/<int:scheduleID>/',views.edit_schedule,name='edit_schedule'),
    #??? should i put <int:nin> here? or sth else?
    path('doc/request_lab/',views.request_lab,name='request_lab'),
    path('lab/test/', views.show_test, name='show_test'),
    path('lab/upload_result/<int:testID>/', views.upload_result, name='upload_result'),
    path('recep/book_appoint/', views.book_appoint, name='recep_book'),
    path('recep/cancel_appoint/', views.cancel_appoint, name='recep_cancel'),
    path('recep/schedule/', views.schedule, name='recep_sche'),
    path('admin/create_account/', views.create_account, name='create_account'),
    path('patient/book_appoint/', views.book_appoint, name='patient_book'),
    path('patient/cancel_appoint/', views.cancel_appoint, name='patient_cancel'),
    path('patient/EHR/<int:nin>/', views.show_EHR, name='patient_EHR'),
    path('patient/edit_EHR/<int:nin>/', views.edit_EHR, name='edit_EHR'),
    # path('accounts/', include('django.contrib.auth.urls')),

]
