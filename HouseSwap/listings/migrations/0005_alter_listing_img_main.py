# Generated by Django 3.2.4 on 2021-06-14 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20210614_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='img_main',
            field=models.ImageField(default='photos/default.png', upload_to='photos/%Y/%m/%d/'),
        ),
    ]
