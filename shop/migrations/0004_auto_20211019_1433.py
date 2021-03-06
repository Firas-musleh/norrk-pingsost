# Generated by Django 3.2.8 on 2021-10-19 12:33

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_product_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='descrip_tr',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_tr',
        ),
        migrations.AddField(
            model_name='product',
            name='product_info_ar',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', null=True, verbose_name='الوصف القصير'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_info_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', null=True, verbose_name='الوصف القصير'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_info_sv',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', null=True, verbose_name='الوصف القصير'),
        ),
    ]
