# Generated by Django 2.2 on 2020-02-13 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_list', '0002_auto_20200212_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='published_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.URLField(null=True),
        ),
    ]