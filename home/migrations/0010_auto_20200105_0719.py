# Generated by Django 2.2.9 on 2020-01-05 07:19

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200105_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxinfo',
            name='body',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.RawHTMLBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=True))]))], blank=True, null=True),
        ),
    ]