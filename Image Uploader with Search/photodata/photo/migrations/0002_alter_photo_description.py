# Generated by Django 4.0.2 on 2022-02-20 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]