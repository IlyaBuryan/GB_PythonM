# Generated by Django 3.2 on 2021-04-18 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('measure', models.CharField(choices=[('KG', 'Kilogramms'), ('UN', 'Units')], max_length=2)),
                ('vendor', models.CharField(max_length=150)),
            ],
        ),
    ]
