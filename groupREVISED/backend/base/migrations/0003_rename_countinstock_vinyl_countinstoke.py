# Generated by Django 3.2.7 on 2021-09-28 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20210928_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vinyl',
            old_name='countInStock',
            new_name='countInStoke',
        ),
    ]
