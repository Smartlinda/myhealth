from django.urls import path,include
from health import views

urlpatterns = [
    path('', views.recephome, name='recephome'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/login/', views.user_login, name='login'),

]
