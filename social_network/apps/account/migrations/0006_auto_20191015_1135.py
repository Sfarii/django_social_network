# Generated by Django 2.2.6 on 2019-10-15 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20191014_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='avatars', verbose_name='Avatar'),
        ),
    ]
