# Generated by Django 2.2.5 on 2020-03-24 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20200309_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='final_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
