# Generated by Django 2.1.5 on 2019-08-05 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InternsOnboardMain', '0003_auto_20190805_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internshippost',
            old_name='discription',
            new_name='description',
        ),
    ]