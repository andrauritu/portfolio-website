# Generated by Django 5.0.7 on 2024-09-10 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_educationsection_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='educationsection',
            options={'ordering': ['order']},
        ),
    ]
