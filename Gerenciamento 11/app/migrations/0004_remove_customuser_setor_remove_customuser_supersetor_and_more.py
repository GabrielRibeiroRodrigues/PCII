# Generated by Django 5.0.6 on 2024-07-26 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_customuser_setor_customuser_supersetor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='Setor',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='SuperSetor',
        ),
        migrations.RemoveField(
            model_name='subsector',
            name='quantidade',
        ),
    ]
