# Generated by Django 3.2.9 on 2021-12-17 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20211217_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disciplines',
            old_name='book',
            new_name='bookis',
        ),
    ]