# Generated by Django 3.2 on 2021-05-17 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_auto_20210516_0431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='content_id',
        ),
    ]