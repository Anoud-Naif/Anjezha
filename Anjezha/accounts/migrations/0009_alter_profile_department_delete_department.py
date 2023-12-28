# Generated by Django 5.0 on 2023-12-28 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_profile_department'),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.department'),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
