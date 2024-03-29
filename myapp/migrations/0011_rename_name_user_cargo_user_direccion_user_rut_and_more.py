# Generated by Django 4.2.6 on 2023-11-17 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_rename_año_manual_manual_año_manual_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='cargo',
        ),
        migrations.AddField(
            model_name='user',
            name='direccion',
            field=models.CharField(default='calle_falsa123', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='rut',
            field=models.CharField(default=2020202020, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='siglas',
            field=models.CharField(default='AA', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='telefono',
            field=models.CharField(default=123414, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='Test_user', max_length=100),
            preserve_default=False,
        ),
    ]
