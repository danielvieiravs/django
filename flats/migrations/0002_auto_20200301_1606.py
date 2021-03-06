# Generated by Django 2.1.1 on 2020-03-01 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='upfront',
        ),
        migrations.AlterField(
            model_name='flat',
            name='bills',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='flat',
            name='n_b',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='flat',
            name='price_one',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='flat',
            name='price_two',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
