# Generated by Django 2.2.3 on 2019-08-24 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_auto_20190824_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtest',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]