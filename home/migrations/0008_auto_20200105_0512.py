# Generated by Django 2.2.9 on 2020-01-05 05:12

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200105_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxinfo',
            name='body',
            field=wagtail.core.fields.StreamField([('icon_link', wagtail.core.blocks.RichTextBlock())]),
        ),
    ]
