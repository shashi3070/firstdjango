# Generated by Django 2.1.2 on 2020-06-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20200615_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customjobinformations',
            name='LastModifiedBy',
            field=models.CharField(default='User', editable=False, max_length=400),
        ),
        migrations.AlterField(
            model_name='matillionjobinformation',
            name='LastModifiedBy',
            field=models.CharField(default='User', editable=False, max_length=400),
        ),
        migrations.AlterField(
            model_name='pythonjobinformations',
            name='LastModifiedBy',
            field=models.CharField(default='User', editable=False, max_length=400),
        ),
        migrations.AlterField(
            model_name='talendjobinformations',
            name='LastModifiedBy',
            field=models.CharField(default='User', editable=False, max_length=400),
        ),
    ]
