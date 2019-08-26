import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'myhealth.settings')
import django
django.setup()
from health.models import User, Department, Disease, Ehr,Hospital,LabTest
from health.models import MedicalSupply,Order,Orderdetail,Phr,Schedule
from django.contrib.auth import get_user_model
from decimal import *
from allauth.account.adapter import DefaultAccountAdapter

def populate():

## making a superuser

    User = get_user_model()

    # email = 'xiong199704242@gmail.com'
    # password = 'asdfghjkl'
    # user_type = 5
    #
    # super = User.objects.create_superuser(email, user_type, password)

    # making some new users for fun

    # doc1 = User.objects.create_user(username='jlennon@beatles.com',email='jlennon@beatles.com',password='glassdoor',user_type=1,first_name='Jlennon',last_name='Beatles')
    # doc2 = User.objects.create_user(username='real@tech.com',email='real@tech.com',password='beautyblender',user_type=1,first_name='Real',last_name='Tech')
    # conduc = User.objects.create_user(username='donald@trump.com',email='donald@trump.com',password='billions',user_type=2,first_name='Donald',last_name='Trump')
    # recep = User.objects.create_user(username='dragrace@vh1.com',email='dragrace@vh1.com',password='kittygirl',user_type=3,first_name='Drag',last_name='Queen')
    # patient1 = User.objects.create_user(username='linda@xiong.com',email='linda@xiong.com',password='xiaotaoqi',user_type=4,first_name='Linda',last_name='Xiong')
    # patient2 = User.objects.create_user(username='adam@burae.com',email='adam@burae.com',password='adamsmith',user_type=4,first_name='Adam',last_name='Burae')
    # patient3 = User.objects.create_user(username='John@sugerman.com',email='John@sugerman.com',password='johnjohnson',user_type=4,first_name='John',last_name='sugerman')
    #
    # #making examples for Hospital
    # hos = Hospital.objects.get_or_create(name="Mary Jane Practice",address="21 Beith Street")[0]
    hos1 = Hospital.objects.get_or_create(name="Gardener Practice",address="19 Beith Street")[0]

    # making examples for Department
    dep1 = Department.objects.get_or_create(name='Cardiology',hospital=hos1,tel_no='01234567891')[0]
    dep2 = Department.objects.get_or_create(name='Anaesthetics',hospital=hos1,tel_no='01233567891')[0]

    # making examples for LabTest
    lab1 = LabTest.objects.get_or_create(patient=User.objects.get(email='linda@xiong.com'),doctor=User.objects.get(email='jlennon@beatles.com'),name='X-ray',conductor=User.objects.get(email='donald@trump.com'))[0]
    lab2 = LabTest.objects.get_or_create(patient=User.objects.get(email='adam@burae.com'),doctor=User.objects.get(email='jlennon@beatles.com'),name='MRI',conductor=User.objects.get(email='donald@trump.com'))[0]

    #making examples for schedules
    s1 = Schedule.objects.get_or_create(patient=User.objects.get(email='linda@xiong.com'),date='25/10/2019',time='10:00')[0]
    s2 = Schedule.objects.get_or_create(patient=User.objects.get(email='adam@burae.com'),date='22/08/2019',time='11:00')[0]
    s3 = Schedule.objects.get_or_create(patient=User.objects.get(email='John@sugerman.com'),date='22/08/2019',time='13:00')[0]

    #making examples for Phr
    p1 = Phr.objects.get_or_create(patient=User.objects.get(email='linda@xiong.com'),weight='45.8',height='160',doctorid=User.objects.get(email='jlennon@beatles.com'))[0]
    p2 = Phr.objects.get_or_create(patient=User.objects.get(email='adam@burae.com'),weight='55',height='170',doctorid=User.objects.get(email='jlennon@beatles.com'))[0]

if __name__=='__main__':
	print("Starting healthDB population script...")
	populate()
