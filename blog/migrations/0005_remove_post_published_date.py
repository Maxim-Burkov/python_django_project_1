# Generated by Django 3.2.12 on 2022-03-27 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220327_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
    ]
