# Generated by Django 2.2.5 on 2020-02-17 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='image',
            field=models.ImageField(upload_to='media/foodimages/'),
        ),
    ]