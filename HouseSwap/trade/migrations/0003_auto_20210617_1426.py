# Generated by Django 3.2.4 on 2021-06-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_offer_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=20),
        ),
        migrations.DeleteModel(
            name='Trade',
        ),
    ]
