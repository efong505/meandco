# Generated by Django 4.2 on 2023-05-03 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_leftimage_project_rightimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='otherdetails',
            new_name='additionalright',
        ),
        migrations.AddField(
            model_name='project',
            name='bottomdetails',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
