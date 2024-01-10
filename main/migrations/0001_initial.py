# Generated by Django 5.0.1 on 2024-01-08 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='Blog Image')),
                ('title', models.CharField(max_length=50, verbose_name='Blog Title')),
                ('text', models.TextField(verbose_name='Blog Text')),
                ('post_date', models.DateField(verbose_name='Blog Post Date')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]
