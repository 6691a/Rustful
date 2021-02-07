# Generated by Django 3.1.5 on 2021-02-02 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('excerpt', models.TextField(null=True)),
                ('content', models.TextField()),
                ('slug', models.SlugField(allow_unicode=True, max_length=255, unique_for_date='created')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
            ],
            options={
                'db_table': 'Post',
                'ordering': ('-created',),
            },
        ),
    ]
