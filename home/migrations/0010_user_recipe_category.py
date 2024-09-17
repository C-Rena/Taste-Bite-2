# Generated by Django 5.0.6 on 2024-09-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_contact_alter_userprofile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_recipe',
            name='category',
            field=models.CharField(choices=[('Seefood', 'Seefood'), ('Soup', 'Soup'), ('Pancakes', 'Pancakes'), ('Meat', 'Meat'), ('Chicken', 'Chicken'), ('Less than 30 min', 'Less than 30 min'), ('Pasta', 'Pasta'), ('Pizza', 'Pizza'), ('Cake', 'Cake'), ('Pastries', 'Pastries'), ('Burger', 'Burger'), ('Vegan', 'Vegan'), ('Desserts', 'Desserts'), ('Smoothies', 'Smoothies'), ('Breakfast', 'Breakfast'), ('Salad', 'Salad'), ('Sandwiches', 'Sandwiches'), ('Waffles', 'Waffles'), ('Ramen', 'Ramen'), ('Dips', 'Dips')], default='Seefood', max_length=50),
        ),
    ]