# Generated by Django 5.0.3 on 2024-03-27 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_cliente_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=11, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]