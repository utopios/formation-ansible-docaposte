# Generated by Django 2.2.8 on 2020-01-15 20:01

from django.db import migrations, models


def cleanup_scan_jts(apps, schema_editor):
    JobTemplate = apps.get_model('main', 'JobTemplate')
    JobTemplate.objects.filter(job_type='scan').update(job_type='run')


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0103_v370_remove_computed_fields'),
    ]

    operations = [
        migrations.RunPython(cleanup_scan_jts),
        migrations.AlterField(
            model_name='jobtemplate',
            name='job_type',
            field=models.CharField(choices=[('run', 'Run'), ('check', 'Check')], default='run', max_length=64),
        ),
    ]
