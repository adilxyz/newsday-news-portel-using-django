# Generated by Django 4.0.5 on 2022-06-20 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_news_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published_date',
            field=models.DateField(auto_created='today'),
        ),
    ]
