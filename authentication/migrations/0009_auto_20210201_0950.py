# Generated by Django 3.0.3 on 2021-02-01 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20210130_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='upload_documents',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
