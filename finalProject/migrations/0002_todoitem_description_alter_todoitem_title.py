# Generated by Django 4.2.4 on 2023-12-06 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalProject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
