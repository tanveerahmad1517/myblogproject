# Generated by Django 2.0.5 on 2018-06-11 16:48

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20180611_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Description'),
        ),
    ]