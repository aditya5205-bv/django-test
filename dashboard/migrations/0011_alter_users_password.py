# Generated by Django 5.1.3 on 2024-11-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_alter_users_image_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(blank=True, default=None, editable=False, max_length=100, null=True),
        ),
    ]
