# Generated by Django 2.2.3 on 2019-08-25 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0011_auto_20190825_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phr',
            name='disease',
            field=models.ForeignKey(blank=True, db_column='disease', null=True, on_delete=django.db.models.deletion.CASCADE, to='health.Disease'),
        ),
    ]
