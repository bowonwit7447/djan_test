# Generated by Django 2.2 on 2020-02-12 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('urlToImage', models.URLField()),
                ('publishedAt', models.DateTimeField()),
            ],
        ),
    ]
