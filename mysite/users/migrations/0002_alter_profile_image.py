# Generated by Django 5.1 on 2024-08-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='sample.jpg', upload_to='profile_pictures'),
        ),
    ]
