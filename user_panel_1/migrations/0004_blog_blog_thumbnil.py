# Generated by Django 3.1.7 on 2021-03-31 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel_1', '0003_auto_20210331_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_thumbnil',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
