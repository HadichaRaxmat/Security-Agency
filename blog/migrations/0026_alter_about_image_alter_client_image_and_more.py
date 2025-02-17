# Generated by Django 5.1.5 on 2025-02-02 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_alter_about_image_alter_client_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='slider_photos/'),
        ),
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='client_photos/'),
        ),
        migrations.AlterField(
            model_name='guard',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='guard_photos/'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='banner_photos/'),
        ),
        migrations.AlterField(
            model_name='touch',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='touch_photos/'),
        ),
    ]
