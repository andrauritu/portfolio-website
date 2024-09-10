# Generated by Django 5.0.7 on 2024-09-10 10:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='education_images/')),
                ('specialisation', models.CharField(blank=True, max_length=255, null=True)),
                ('gpa', models.CharField(blank=True, max_length=10, null=True)),
                ('relevant_subjects', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('extra', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
