# Generated by Django 5.0.6 on 2024-09-07 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_favorite'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together=set(),
        ),
    ]
