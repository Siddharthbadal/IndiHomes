# Generated by Django 4.0.4 on 2022-09-10 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='email',
            field=models.URLField(max_length=50),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='facebook',
            field=models.URLField(max_length=50),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='insta',
            field=models.URLField(max_length=50),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='twitter',
            field=models.URLField(max_length=50),
        ),
    ]
