# Generated by Django 2.2.3 on 2019-07-27 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'doctor'), (2, 'labPeople'), (3, 'receptionist'), (4, 'patient'), (5, 'admin')], null=True),
        ),
    ]