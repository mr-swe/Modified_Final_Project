# Generated by Django 3.1.3 on 2020-12-14 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_subscriber'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subscriber',
        ),
    ]
