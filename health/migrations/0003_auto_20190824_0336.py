# Generated by Django 2.2.3 on 2019-08-24 03:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_auto_20190823_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labtest',
            name='conductor',
            field=models.ForeignKey(blank=True, db_column='conductor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='conduct', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='notes',
            field=models.TextField(blank=True, max_length=65535, null=True),
        ),
    ]
