# Generated by Django 4.1.3 on 2022-11-14 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('streams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='stream',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='streams.stream'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stream',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streams', to=settings.AUTH_USER_MODEL),
        ),
    ]