from django.conf.urls import url
from health import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
