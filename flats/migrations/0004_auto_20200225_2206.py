# Generated by Django 2.1.1 on 2020-02-25 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flats', '0003_auto_20200222_1211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='number_bedrooms',
            new_name='n_b',
        ),
        migrations.RenameField(
            model_name='flat',
            old_name='length',
            new_name='upfront',
        ),
        migrations.AddField(
            model_name='flat',
            name='min_length',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='flat',
            name='bills',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]