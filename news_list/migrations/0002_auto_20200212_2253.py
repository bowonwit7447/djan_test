# Generated by Django 2.2 on 2020-02-12 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='urlToImage',
            new_name='image_url',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='publishedAt',
            new_name='published_at',
        ),
    ]
