# Generated by Django 3.1.7 on 2021-05-19 05:29

from django.db import migrations, models
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('user_panel_1', '0019_auto_20210505_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_updateDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_tags',
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
