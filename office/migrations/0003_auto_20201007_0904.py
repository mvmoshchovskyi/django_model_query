# Generated by Django 3.1.2 on 2020-10-07 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0002_auto_20201007_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='office.officemodel'),
        ),
    ]
