# Generated by Django 3.2.20 on 2023-07-18 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoplugins', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plugin',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pluginpoint',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
