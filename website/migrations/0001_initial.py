# Generated by Django 2.1.2 on 2020-06-15 05:44

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Custom_Run_JobHistory',
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
        migrations.CreateModel(
            name='CustomJobInformations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobName', models.CharField(max_length=1000)),
                ('HtmlData', models.TextField()),
                ('Comp_Seq', models.CharField(max_length=1000)),
                ('Comp_Data', models.CharField(max_length=1000)),
                ('Enable', models.BooleanField(default=True)),
                ('Day_of_Week', models.CharField(default='mon,tue,wed,thu,fri,sat,sun', max_length=50)),
                ('timezone', models.CharField(default='Asia/Kolkata', max_length=50)),
                ('Hours', models.CharField(default='23:00', max_length=50)),
                ('Minutes', models.CharField(default='46', max_length=50)),
                ('EndDate', models.DateField(default=datetime.date.today)),
                ('MatIP', models.CharField(default='172.31.12.129', max_length=100)),
                ('MatGroup', models.CharField(default='Outbound_Process', max_length=1000)),
                ('MatProject', models.CharField(default='Outbound_Process', max_length=1000)),
                ('MatVersion', models.CharField(default='default', max_length=1000)),
                ('MatEnvironment', models.CharField(default='OutBound', max_length=1000)),
                ('user', models.CharField(default='Test_User3', max_length=50)),
                ('password', models.CharField(default='admin123', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='index_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
                ('subsubject', models.TextField()),
                ('descriptions', models.TextField()),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Matilion_Run_JobHistory',
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
        migrations.CreateModel(
            name='MatillionJobInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP', models.CharField(default='172.31.12.129', max_length=400)),
                ('JobName', models.CharField(max_length=1000)),
                ('projectName', models.CharField(max_length=400)),
                ('version', models.CharField(default='default', max_length=50)),
                ('user', models.CharField(default='Test_User3', max_length=50)),
                ('password', models.CharField(default='admin123', max_length=50)),
                ('MatGroup', models.CharField(default='Outbound_Process', max_length=1000)),
                ('Environment', models.CharField(default='OutBound', max_length=50)),
                ('Enable', models.BooleanField(default=True)),
                ('Day_of_Week', models.CharField(default='mon,tue,wed,thu,fri,sat,sun', max_length=50)),
                ('timezone', models.CharField(default='Asia/Kolkata', max_length=50)),
                ('Hours', models.CharField(default='23:00', max_length=50)),
                ('Minutes', models.CharField(default='46', max_length=50)),
                ('EndDate', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='MatJobInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP', models.CharField(default='172.31.12.129', max_length=400)),
                ('JobName', models.TextField(max_length=400)),
                ('projectName', models.CharField(max_length=400)),
                ('version', models.CharField(default='default', max_length=50)),
                ('user', models.CharField(default='Test_User3', max_length=50)),
                ('password', models.CharField(default='admin123', max_length=50)),
                ('Environment', models.CharField(default='OutBound', max_length=50)),
                ('Enable', models.BooleanField(default=True)),
                ('Day_of_Week', models.CharField(default='mon,tue,wed,thu,fri,sat,sun', max_length=50)),
                ('Hours', models.CharField(default='23:00', max_length=50)),
                ('Minutes', models.CharField(default='46', max_length=50)),
                ('EndDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Python_Run_JobHistory',
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
        migrations.CreateModel(
            name='PythonJobInformations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobName', models.CharField(max_length=1000)),
                ('Enable', models.BooleanField(default=True)),
                ('Day_of_Week', models.CharField(default='mon,tue,wed,thu,fri,sat,sun', max_length=50)),
                ('timezone', models.CharField(default='Asia/Kolkata', max_length=50)),
                ('Hours', models.CharField(default='23:00', max_length=50)),
                ('Minutes', models.CharField(default='46', max_length=50)),
                ('EndDate', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Talend_Run_JobHistory',
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
        migrations.CreateModel(
            name='TalendJobInformations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobName', models.CharField(max_length=1000)),
                ('EndPoint', models.CharField(max_length=3000)),
                ('Enable', models.BooleanField(default=True)),
                ('Day_of_Week', models.CharField(default='mon,tue,wed,thu,fri,sat,sun', max_length=50)),
                ('timezone', models.CharField(default='Asia/Kolkata', max_length=50)),
                ('Hours', models.CharField(default='23:00', max_length=50)),
                ('Minutes', models.CharField(default='46', max_length=50)),
                ('EndDate', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
