# Generated by Django 3.2.4 on 2021-06-14 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='photos/default.png', upload_to='photos/%Y/%m/%d/'),
        ),
    ]
