# Generated by Django 3.1.1 on 2020-09-18 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooddatas',
            name='GOOD',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fooddatas',
            name='NOT_GOOD',
            field=models.IntegerField(default=0),
        ),
    ]
