# Generated by Django 3.2.9 on 2021-12-17 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211217_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='book',
        ),
        migrations.AddField(
            model_name='disciplines',
            name='book',
            field=models.TextField(default='', max_length=120000),
        ),
    ]