# Generated by Django 5.1.6 on 2025-02-28 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='blog_id',
            new_name='post',
        ),
    ]
