# Generated by Django 2.2.9 on 2020-01-05 02:40

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200103_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxinfo',
            name='body',
            field=wagtail.core.fields.StreamField([('icon_link', wagtail.core.blocks.RichTextBlock()), ('raw_html', wagtail.core.blocks.RawHTMLBlock())]),
        ),
    ]
