# Generated by Django 5.1.6 on 2025-02-21 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_mail_usuarios_correo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='carrera',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='correo',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='matricula',
            field=models.CharField(default='SIN_MATRICULA', max_length=100),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='semestre',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
