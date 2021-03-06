# Generated by Django 2.2.9 on 2020-01-05 07:47

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20200105_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxinfo',
            name='body',
            field=wagtail.core.fields.StreamField([('tax_info_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.RawHTMLBlock(help_text='Add your svg image', required=True)), ('text', wagtail.core.blocks.RichTextBlock(help_text='Add Hyperlink', required=True))]))], blank=True, null=True),
        ),
    ]
