# Generated by Django 3.1.7 on 2021-04-13 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel_1', '0010_auto_20210413_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blog_thumbnil',
        ),
    ]
