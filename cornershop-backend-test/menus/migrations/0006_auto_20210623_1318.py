# Generated by Django 3.0.8 on 2021-06-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0005_menu_menu_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='available',
            field=models.BooleanField(default=True, verbose_name='available'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
