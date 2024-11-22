# Generated by Django 5.1.3 on 2024-11-19 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_users_created_at_alter_users_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_active',
            field=models.SmallIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_deleted',
            field=models.SmallIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]