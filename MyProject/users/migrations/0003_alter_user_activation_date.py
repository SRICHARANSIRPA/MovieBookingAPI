# Generated by Django 4.0 on 2021-12-20 14:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_activation_date_alter_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
