# Generated by Django 4.2.6 on 2023-11-03 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
