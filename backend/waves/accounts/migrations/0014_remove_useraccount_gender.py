# Generated by Django 4.2.5 on 2023-11-07 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_useraccount_gender_useraccount_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='gender',
        ),
    ]