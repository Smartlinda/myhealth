# Generated by Django 2.2.3 on 2019-08-24 08:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0005_auto_20190824_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labtest',
            name='report',
            field=models.FileField(blank=True, null=True, upload_to='report/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]
