# Generated by Django 4.2 on 2023-05-02 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_alter_workexperience_end_alter_workexperience_start'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workexperience',
            options={'ordering': ['-start', 'end']},
        ),
        migrations.RemoveIndex(
            model_name='workexperience',
            name='resume_work_start_96f4f7_idx',
        ),
        migrations.AddIndex(
            model_name='workexperience',
            index=models.Index(fields=['-start'], name='resume_work_start_566c28_idx'),
        ),
    ]
