# Generated by Django 2.1.2 on 2020-06-23 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20200622_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='DashBoard_History_Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobID', models.CharField(max_length=800)),
                ('JobName', models.CharField(max_length=800)),
                ('StartTime', models.CharField(default='default', max_length=500)),
                ('EndTime', models.CharField(default='default', max_length=500)),
                ('Status', models.CharField(default='Failed', max_length=500)),
                ('RunDate', models.CharField(default='default', max_length=500)),
                ('Sche_or_Manu', models.CharField(default='Schedule', max_length=500)),
                ('description', models.CharField(default='Success', max_length=500)),
            ],
        ),
    ]
