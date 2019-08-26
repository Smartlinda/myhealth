import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'myhealth.settings')
import django
django.setup()
from health.models import User, Department, Disease, Ehr,Hospital,LabTest
from health.models import MedicalSupply,Order,Orderdetail,Phr,Schedule
from django.contrib.auth import get_user_model
from decimal import *

def populate():

## making a superuser

    # User = get_user_model()
    #
    # email = 'xiong199704242@gmail.com'
    # password = 'asdfghjkl'
    # user_type = 5
    #
    # super = User.objects.create_superuser(email, user_type, password)
    #
    # # making some new users for fun
    #
    # doc1 = User.objects.signup(email='jlennon@beatles.com',password='glassdoor',user_type=1)
    # doc2 = User.objects.signup(email='real@tech.com',password='beautyblender',user_type=1)
    # conduc = User.objects.signup(email='donald@trump.com',password='billions',user_type=2)
    # recep = User.objects.signup(email='dragrace@vh1.com',password='kittygirl',user_type=3)
    # patient1 = User.objects.create_user(email='linda@xiong.com',password='xiaotaoqi',user_type=4)
    # patient2 = User.objects.create_user(email='adam@burae.com',password='adamsmith',user_type=4)
    # patient3 = User.objects.create_user(email='John@sugerman.com',password='johnjohnson',user_type=4)

    # making examples for Hospital
    # hos = Hospital.objects.create(name="Mary Jane Practice",address="21 Beith Street")
    hos1 = Hospital.objects.create(name="Gardener Practice",address="19 Beith Street")

    # making examples for Department
    dep1 = Department.objects.create(name='Cardiology',hospital=hos1,tel_no='01234567891')
    dep2 = Department.objects.create(name='Anaesthetics',hospital=hos1,tel_no='01233567891')

    # making examples for LabTest
    lab1 = LabTest.objects.get_or_create(patient=User.objects.get(email='linda@xiong.com'),doctor=User.objects.get(email='jlennon@beatles.com'),name='X-ray',conductor=User.objects.get(email='donald@trump.com'))
    lab2 = LabTest.objects.get_or_create(patient=User.objects.get(email='adam@burae.com'),doctor=User.objects.get(email='jlennon@beatles.com'),name='MRI',conductor=User.objects.get(email='donald@trump.com'))

    # making examples for Disease
    ibs = Disease.objects.create(name="Irritable bowel syndrome")
    acne = Disease.objects.create(name="Acne")
    bv = Disease.objects.create(name="Bacterial Vaginosis")
    coma = Disease.objects.create(name="Coma")
    flu = Disease.objects.create(name="flu")
    diabetes = Disease.objects.create(name="Diabetes")

    #making examples for schedules
    s1 = Schedule.objects.create(patient=User.objects.get(email='linda@xiong.com'),date='2019-10-25',time='10:00')
    s2 = Schedule.objects.create(patient=User.objects.get(email='adam@burae.com'),date='2019-08-22',time='11:00')
    s3 = Schedule.objects.create(patient=User.objects.get(email='John@sugerman.com'),date='2019-08-22',time='13:00')

    #making examples for medicalSupply
    syringe = MedicalSupply.objects.create(name='syringe',stock=100)
    ibruprofen = MedicalSupply.objects.create(name='ibruprofen',stock=1000)
    iodine = MedicalSupply.objects.create(name='iodine',stock=50)
    mebeverine = MedicalSupply.objects.create(name='mebeverine',stock=2000)

    #making examples for Order
    o1 = Order.objects.create(datetime='2019-11-28 08:00+00:00')
    o2 = Order.objects.create(datetime='2019-01-15 14:00+00:00')
    o3 = Order.objects.create(datetime='2019-05-18 13:00+00:00')

    #making examples for OrderDetail
    od1 = Orderdetail.objects.get_or_create(orderid=o1,medicalsupply=syringe,amount=500)
    od2 = Orderdetail.objects.get_or_create(orderid=o1,medicalsupply=iodine,amount=500)
    od3 = Orderdetail.objects.get_or_create(orderid=o1,medicalsupply=ibruprofen,amount=500)

    #making examples for Phr
    p1 = Phr.objects.get_or_create(patient=User.objects.get(email='linda@xiong.com'),weight='45.8',height='160',doctorid=User.objects.get(email='jlennon@beatles.com'),disease=ibs)
    p2 = Phr.objects.get_or_create(patient=User.objects.get(email='adam@burae.com'),weight='55',height='170',doctorid=User.objects.get(email='jlennon@beatles.com'),disease=bv)

    # making examples for Ehr
    ehr1 = Ehr.objects.get_or_create(schedule=s1,medicalsupply=ibruprofen,amount=10)
    ehr2 = Ehr.objects.get_or_create(schedule=s2,medicalsupply=mebeverine,amount=30)
    ehr3 = Ehr.objects.get_or_create(schedule=s3,medicalsupply=iodine,amount=2)

if __name__=='__main__':
	print("Starting healthDB population script...")
	populate()
