# Generated by Django 2.0.5 on 2018-05-27 07:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_confirmed',
            field=models.BooleanField(default=False, verbose_name='验证邮箱'),
        ),
    ]