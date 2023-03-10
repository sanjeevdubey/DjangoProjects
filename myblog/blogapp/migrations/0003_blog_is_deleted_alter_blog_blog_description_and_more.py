# Generated by Django 4.1.4 on 2022-12-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_blog_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='featured_image',
            field=models.ImageField(default=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_description',
            field=models.TextField(),
        ),
    ]
