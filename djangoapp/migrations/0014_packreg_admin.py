# Generated by Django 5.2 on 2025-05-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0013_alter_packreg_amount_alter_packreg_days_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='packreg',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]
