# Generated by Django 5.1 on 2024-08-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://cookinupastorm.biz/wp-content/uploads/2023/04/EmptyDinnerPlates.jpg', max_length=500),
        ),
    ]
