# Generated by Django 2.1.1 on 2018-10-07 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0005_auto_20180910_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='submission_deadline',
            field=models.CharField(max_length=25),
        ),
    ]