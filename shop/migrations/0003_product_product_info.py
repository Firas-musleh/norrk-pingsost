# Generated by Django 3.2.8 on 2021-10-18 23:51

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_info',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', null=True, verbose_name='الوصف القصير'),
        ),
    ]
