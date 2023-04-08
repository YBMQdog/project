# Generated by Django 4.1.5 on 2023-02-25 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0012_remove_project_metrological_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Metrological',
            field=models.CharField(default=1, max_length=200, verbose_name='Metrological'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='SingleDetermination',
            field=models.CharField(default=1, max_length=200, verbose_name='SingleDetermination'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='TestParameters',
            field=models.CharField(default=1, max_length=200, verbose_name='TestParameters'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='TestRequirements',
            field=models.CharField(default=1, max_length=200, verbose_name='TestRequirements'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='TestValueError',
            field=models.CharField(default=1, max_length=200, verbose_name='TestValueError'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='TestValues',
            field=models.CharField(default=1, max_length=200, verbose_name='TestValues'),
            preserve_default=False,
        ),
    ]