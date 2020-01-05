from wagtail.core import blocks

class TaxInfoBlock(blocks.StructBlock):
    """Title and text and nothing else."""

    title = blocks.RawHTMLBlock(required=True, help_text="Add your svg image")
    text = blocks.RichTextBlock(required=True, help_text="Add Hyperlink")

    class Meta:  # noqa
        template = "streams/tax_info_block.html"
        icon = "edit"
        label = "Tax Info"