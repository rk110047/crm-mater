# Generated by Django 3.0.3 on 2021-01-30 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210130_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='upload_documents',
            field=models.FileField(blank=True, default='', upload_to='static'),
        ),
    ]