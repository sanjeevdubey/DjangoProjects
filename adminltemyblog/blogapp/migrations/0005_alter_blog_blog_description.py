# Generated by Django 4.1.4 on 2022-12-17 19:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_blog_blogtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]