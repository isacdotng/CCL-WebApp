# Generated by Django 4.2.6 on 2023-11-01 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_client'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjPhoto',
            new_name='ProjectPhoto',
        ),
    ]
