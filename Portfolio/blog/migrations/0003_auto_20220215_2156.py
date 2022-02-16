# Generated by Django 3.2 on 2022-02-15 18:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220215_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='discription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
