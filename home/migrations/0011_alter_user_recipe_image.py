# Generated by Django 5.0.6 on 2024-09-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_user_recipe_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_recipe',
            name='image',
            field=models.FileField(upload_to='Recipe imgs'),
        ),
    ]