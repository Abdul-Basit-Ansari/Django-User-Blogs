# Generated by Django 3.2.8 on 2022-04-05 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountdata', '0007_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='content1',
            new_name='content',
        ),
    ]
