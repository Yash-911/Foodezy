# Generated by Django 2.2.5 on 2020-02-17 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_recipe', '0002_auto_20200217_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='image',
            field=models.ImageField(upload_to='foodimages/'),
        ),
    ]
