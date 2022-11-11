# Generated by Django 4.1.3 on 2022-11-11 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(choices=[('product', 'Product'), ('community', 'Community')], max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
