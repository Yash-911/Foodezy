# Generated by Django 2.2.5 on 2020-03-24 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_auto_20200324_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
