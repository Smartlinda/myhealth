import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'myhealth.settings')
import django
django.setup()
from health.models import User, Department, Staff, Disease, Ehr,Hospital,LabTest
from health.models import MedicalSupply,Order,Orderdetail,Phr,Patient,Schedule
from django.contrib.auth import get_user_model

def populate():

## making a superuser

    # User = get_user_model()

    # email = 'xiong199704242@gmail.com'
    # password = 'asdfghjkl'
    # user_type = 5
    #
    # super = User.objects.create_superuser(email, password, user_type)
    # s_super = Staff.objects.get_or_create(user=super)

    # making some new users for fun

    doc = User.objects.create_user(email='jlennon@beatles.com',password='glassdoor',user_type=1)
    s_doc = Staff.objects.get_or_create(user=doc)
    conduc = User.objects.create_user(email='donald@trump.com',password='billions',user_type=2)
    s_conduc = Staff.objects.get_or_create(user=conduc)
    recep = User.objects.create_user(email='dragrace@vh1.com',password='kittygirl',user_type=3)
    s_recep = Staff.objects.get_or_create(user=recep)
    patient1 = User.objects.create_user(email='linda@xiong.com',password='lindaxiong',user_type=4)
    p_patient1 = Patient.objects.get_or_create(user=patient1)
    patient2 = User.objects.create_user(email='adam@burae.com',password='adamsmith',user_type=4)
    p_patient2 = Patient.objects.get_or_create(user=patient2)
    patient3 = User.objects.create_user(email='John@sugerman.com',password='johnjohnson',user_type=4)
    p_patient3 = Patient.objects.get_or_create(user=patient3)


    # making examples for Department
    dep1 = Department.objects.get_or_create(name='Cardiology',hospitalid=hos,tel_no='01234567891')
    dep2 = Department.objects.get_or_create(name='Anaesthetics',hospitalid=hos,tel_no='01233567891')

    # making examples for Hospital
    hos = Hospital.objects.get_or_create(name="Mary Jane Practice",address="21 Beith Street")

    # making examples for LabTest
    lab1 = LabTest.objects.get_or_create(patient=patient1,doctor=doc,name='X-ray',conductor=conduc)
    lab2 = LabTest.objects.get_or_create(patient=patient2,doctor=doc,name='MRI',conductor=conduc)

    # making examples for Disease
    ibs = Disease.objects.get_or_create(name="Irritable bowel syndrome")
    acne = Disease.objects.get_or_create(name="Acne")
    bv = Disease.objects.get_or_create(name="Bacterial Vaginosis")
    coma = Disease.objects.get_or_create(name="Coma")
    flu = Disease.objects.get_or_create(name="flu")
    diabetes = Disease.objects.get_or_create(name="Diabetes")

    #making examples for schedules
    s1 = Schedule.objects.get_or_create(patient=patient1,date_time='2019-10-25 10:00')
    s2 = Schedule.objects.get_or_create(patient=patient2,date_time='10-25-2019 11:00')
    s3 = Schedule.objects.get_or_create(patient=patient3,date_time='10-25-2019 13:00')

    #making examples for medicalSupply
    syringe = MedicalSupply.objects.get_or_create(name='syringe',stock=100)
    ibruprofen = MedicalSupply.objects.get_or_create(name='ibruprofen',stock=1000)
    iodine = MedicalSupply.objects.get_or_create(name='iodine',stock=50)
    mebeverine = MedicalSupply.objects.get_or_create(name='mebeverine',stock=2000)

    #making examples for Order
    o1 = Order.objects.get_or_create(datetime='2019-11-28 08:00')
    o2 = Order.objects.get_or_create(datetime='2019-01-15 14:00')
    o3 = Order.objects.get_or_create(datetime='2019-05-18 13:00')

    #making examples for OrderDetail
    od1 = OrderDetail.objects.get_or_create(orderid=o1,medicalsupply=syringe,amount=500)
    od2 = OrderDetail.objects.get_or_create(orderid=o1,medicalsupply=iodine,amount=500)
    od3 = OrderDetail.objects.get_or_create(orderid=o1,medicalsupply=ibruprofen,amount=500)

    #making examples for Phr
    p1 = Phr.objects.get_or_create(patient=patient1,weight=45.8,height=160,doctorid=doc,disease=ibs)
    p2 = Phr.objects.get_or_create(patient=patient1,weight=55,height=170,doctorid=doc,disease=bv)

    # making examples for Ehr
    ehr1 = Ehr.objects.get_or_create(schedule=s1,medicalsupply=ibruprofen,amount=10)
    ehr2 = Ehr.objects.get_or_create(schedule=s2,medicalsupply=mebeverine,amount=30)
    ehr3 = Ehr.objects.get_or_create(schedule=s3,medicalsupply=iodine,amount=2)

if __name__=='__main__':
	print("Starting healthDB population script...")
	populate()
