# Generated by Django 2.0.8 on 2019-12-23 15:39

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20191223_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='button',
            field=wagtail.core.fields.RichTextField(default=''),
        ),
    ]
