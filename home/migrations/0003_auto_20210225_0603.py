# Generated by Django 3.1.6 on 2021-02-25 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='des',
            new_name='message',
        ),
    ]