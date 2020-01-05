from django.db import models
from django.http import HttpResponseRedirect

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core import hooks
from smithsite import blockss

class HomePage(Page):
    body = StreamField([
        ('heading', blocks.RichTextBlock(classname="full")),
        ('image', ImageChooserBlock()),
    ], default='')
    button = RichTextField(blank=False, default='')
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    	FieldPanel('button', classname="full"),
    ]


class Aptm(Page):
	header = RichTextField(blank=False)
	body = StreamField([
		('heading', blocks.CharBlock(classname="full title")),
		('paragraph', blocks.RichTextBlock()),
	], default='')
	content_panels = Page.content_panels + [
        FieldPanel('header', classname="full"),
        StreamFieldPanel('body', classname="full"),
    ]


class TaxInfo(Page):
	# body = StreamField([
 #        ('icon_link', blocks.RichTextBlock()),
 #    ])

    body = StreamField([
        ("tax_info_block", blockss.TaxInfoBlock())
        ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full"),
    ]

@hooks.register('register_rich_text_features')
def register_blockquote_feature(features):
    features.default_features.append('code')

		
class Upload(Page):
	header = RichTextField(blank=False)
	body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
    ])
	content_panels = Page.content_panels + [
    	FieldPanel('header', classname="full"),
        StreamFieldPanel('body', classname="full"),
    ]


class Pay(Page):
	header = RichTextField(blank=False)
	body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])
	content_panels = Page.content_panels + [
    	FieldPanel('header', classname="full"),
        StreamFieldPanel('body', classname="full"),
    ]



