# Generated by Django 5.1.5 on 2025-02-20 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0042_usercontact_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercontact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
