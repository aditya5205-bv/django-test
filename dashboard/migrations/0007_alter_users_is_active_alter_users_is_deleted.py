# Generated by Django 5.1.3 on 2024-11-20 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_users_created_at_alter_users_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_deleted',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
