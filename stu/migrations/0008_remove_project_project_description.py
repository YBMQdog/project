# Generated by Django 4.1.5 on 2023-02-04 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0007_remove_project_project_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_description',
        ),
    ]