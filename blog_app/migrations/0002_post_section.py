# Generated by Django 3.2.6 on 2021-08-13 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='section',
            field=models.CharField(default='poem', max_length=100),
            preserve_default=False,
        ),
    ]
