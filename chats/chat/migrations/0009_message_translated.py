# Generated by Django 3.1.7 on 2021-05-30 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doubtsBlog', '0008_remove_message_reciever'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='translated',
            field=models.TextField(default='n'),
            preserve_default=False,
        ),
    ]