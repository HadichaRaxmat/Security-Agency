# Generated by Django 5.1.5 on 2025-02-02 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_menu_options_menu_url_alter_menu_menu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={},
        ),
        migrations.RemoveField(
            model_name='menu',
            name='url',
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu',
            field=models.CharField(max_length=100),
        ),
    ]
