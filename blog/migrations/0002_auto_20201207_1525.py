# Generated by Django 3.1.4 on 2020-12-07 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyBlog',
            new_name='Blog',
        ),
    ]