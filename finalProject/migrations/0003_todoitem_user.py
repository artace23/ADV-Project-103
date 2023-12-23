# Generated by Django 4.2.4 on 2023-12-13 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finalProject', '0002_todoitem_description_alter_todoitem_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]