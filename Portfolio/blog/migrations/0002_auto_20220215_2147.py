# Generated by Django 3.2 on 2022-02-15 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blogmodel',
            name='url',
        ),
    ]
