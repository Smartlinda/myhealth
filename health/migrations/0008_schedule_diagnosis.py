# Generated by Django 2.2.3 on 2019-08-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0007_auto_20190824_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='diagnosis',
            field=models.TextField(blank=True, max_length=65535, null=True),
        ),
    ]