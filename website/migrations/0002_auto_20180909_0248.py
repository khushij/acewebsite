# Generated by Django 2.1.1 on 2018-09-08 21:18

import cloudinary.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500)),
                ('agenda_type', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('time', models.TimeField(blank=True, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('picture', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
            ],
        ),
        migrations.DeleteModel(
            name='Calendar',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_date',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='desc',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='photos',
        ),
        migrations.RemoveField(
            model_name='event',
            name='poc',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='project',
            name='screenshot',
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='project',
            name='when',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='image',
        ),
        migrations.AlterField(
            model_name='project',
            name='created_by',
            field=models.ManyToManyField(blank=True, null=True, to='portalapp.ACEUserProfile'),
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.AddField(
            model_name='event',
            name='images',
            field=models.ManyToManyField(to='website.Image'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ManyToManyField(to='website.Image'),
        ),
    ]
