# Generated by Django 2.2.6 on 2019-10-15 11:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='rooms', verbose_name='Room avatar'),
        ),
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
