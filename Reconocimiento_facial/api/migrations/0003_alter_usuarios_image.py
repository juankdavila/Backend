# Generated by Django 5.1.6 on 2025-02-21 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_usuarios_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics/'),
        ),
    ]
