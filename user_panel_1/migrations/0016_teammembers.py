# Generated by Django 3.1.7 on 2021-05-05 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel_1', '0015_auto_20210503_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tm_priority', models.IntegerField()),
                ('tm_name', models.CharField(max_length=80)),
                ('tm_bio', models.CharField(max_length=500)),
                ('tm_email', models.EmailField(max_length=254)),
                ('tm_github', models.CharField(max_length=100)),
                ('tm_linkedin', models.CharField(max_length=100)),
                ('tm_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
