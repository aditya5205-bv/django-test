# Generated by Django 5.1.3 on 2024-11-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, default=None, max_length=20, unique=True),
        ),
    ]