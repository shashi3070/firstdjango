# Generated by Django 2.1.2 on 2020-06-15 05:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_matillionjobinformation_lastmodified'),
    ]

    operations = [
        migrations.AddField(
            model_name='customjobinformations',
            name='LastModified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='pythonjobinformations',
            name='LastModified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='talendjobinformations',
            name='LastModified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]