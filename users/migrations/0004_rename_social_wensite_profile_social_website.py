# Generated by Django 4.0.5 on 2022-06-18 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_wensite',
            new_name='social_website',
        ),
    ]