# Generated by Django 5.1.3 on 2024-11-19 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_users_first_signup_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=None, null=True, verbose_name='timestamp'),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_active',
            field=models.SmallIntegerField(default=None, null=True, verbose_name='tinyint'),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_deleted',
            field=models.SmallIntegerField(default=None, null=True, verbose_name='tinyint'),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(default=None, null=True, verbose_name='timestamp'),
        ),
    ]