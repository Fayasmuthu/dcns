# Generated by Django 5.0.1 on 2024-01-17 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_enquiryform_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiryform',
            name='services',
            field=models.CharField(max_length=100),
        ),
    ]
