# Generated by Django 4.2.4 on 2023-12-13 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalProject', '0005_alter_todoitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='user',
        ),
    ]