# Generated by Django 4.2 on 2023-05-03 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0018_alter_quote_requester'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='quoted',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Reviewing', 'Reviewing'), ('Approved', 'Approved')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='quote',
            name='stat',
            field=models.CharField(choices=[('New Site', 'Newsite'), ('Existing Site', 'Existing')], default='New Site', max_length=20),
        ),
    ]
