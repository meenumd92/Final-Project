# Generated by Django 5.2 on 2025-05-20 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0015_rename_admin_packreg_approval'),
    ]

    operations = [
        migrations.AddField(
            model_name='packreg',
            name='img',
            field=models.ImageField(null=True, upload_to='gallery/'),
        ),
    ]
