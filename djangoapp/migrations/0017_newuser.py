# Generated by Django 5.2 on 2025-05-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0016_packreg_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.TextField()),
                ('username', models.TextField()),
                ('password', models.CharField()),
            ],
        ),
    ]
