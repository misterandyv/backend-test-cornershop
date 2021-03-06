# Generated by Django 3.0.8 on 2021-06-22 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menus", "0002_auto_20210622_1515"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="options",
            field=models.ManyToManyField(
                blank=True,
                db_table="menus_menus_options",
                related_name="menu_options",
                to="menus.MenuOption",
            ),
        ),
    ]
