# Generated by Django 4.1.3 on 2022-11-09 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('give_away', models.BooleanField(default=False)),
                ('get_price_offer', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('latitude_to_trade', models.CharField(max_length=100)),
                ('longitude_to_trade', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]