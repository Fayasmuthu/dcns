# Generated by Django 5.0.1 on 2024-01-16 13:24

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='updates/')),
                ('name', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=500)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('is_service', models.BooleanField(default=False)),
                ('is_home', models.BooleanField(default=False)),
                ('is_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Update',
                'verbose_name_plural': 'Updates',
                'ordering': ['id'],
            },
        ),
    ]