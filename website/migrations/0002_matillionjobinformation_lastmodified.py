# Generated by Django 2.1.2 on 2020-06-15 05:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matillionjobinformation',
            name='LastModified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
