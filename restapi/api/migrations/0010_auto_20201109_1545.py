# Generated by Django 3.1.1 on 2020-11-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20201108_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooddatas',
            name='BSSH_NM',
            field=models.CharField(max_length=200),
        ),
    ]
