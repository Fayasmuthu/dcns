# Generated by Django 5.0.1 on 2024-01-19 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updates',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
