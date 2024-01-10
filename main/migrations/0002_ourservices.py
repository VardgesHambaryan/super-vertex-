# Generated by Django 5.0.1 on 2024-01-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.TextField(verbose_name='First Text')),
                ('text2', models.TextField(verbose_name='Second Text')),
            ],
            options={
                'verbose_name': 'OurServices',
                'verbose_name_plural': 'OurServices',
            },
        ),
    ]
