# Generated by Django 4.2.1 on 2023-08-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('USER', 'USER'), ('ADMIN', 'ADMIN')], default='USER', max_length=25),
        ),
    ]
