# Generated by Django 3.1.7 on 2021-05-29 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doubtsBlog', '0005_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='content',
            field=models.TextField(default='empty'),
            preserve_default=False,
        ),
    ]