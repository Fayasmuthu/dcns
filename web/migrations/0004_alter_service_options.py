# Generated by Django 5.0.1 on 2024-01-16 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_rename_update_service'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['id'], 'verbose_name': 'service', 'verbose_name_plural': 'services'},
        ),
    ]