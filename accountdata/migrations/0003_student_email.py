# Generated by Django 3.2.8 on 2022-03-24 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountdata', '0002_student_student_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
    ]
