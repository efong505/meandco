# Generated by Django 4.2 on 2023-05-02 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='title',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]
