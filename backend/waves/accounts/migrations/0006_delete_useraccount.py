# Generated by Django 4.2.5 on 2023-09-27 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_useraccount_delete_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAccount',
        ),
    ]
