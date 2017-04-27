# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-24 20:44
from __future__ import unicode_literals

from django.db import migrations
import khanatek.core.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks
import wagtailmarkdown.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_articlepage_streamfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('alignment', khanatek.core.models.ImageFormatChoiceBlock()), ('caption', wagtail.wagtailcore.blocks.CharBlock()), ('attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))), label='Aligned image')), ('wide_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()),), label='Wide image')), ('bustout', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('text', wagtail.wagtailcore.blocks.RichTextBlock())))), ('pullquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.CharBlock(classname='quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='code')), ('link', wagtail.wagtailcore.blocks.URLBlock()), ('markdown', wagtailmarkdown.fields.MarkdownBlock(icon='code')))),
        ),
        migrations.AlterField(
            model_name='servicepage',
            name='streamfield',
            field=wagtail.wagtailcore.fields.StreamField((('case_studies', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('intro', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('case_studies', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('page', wagtail.wagtailcore.blocks.PageChooserBlock('core.ProjectPage')), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('descriptive_title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))))))))), ('highlights', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('intro', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('highlights', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.TextBlock()))))), ('pull_quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.CharBlock(classname='quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())), template='blocks/pull_quote_block.html')), ('process', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('intro', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('steps', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('subtitle', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Paste SVG code here', max_length=9000, required=True)), ('description', wagtail.wagtailcore.blocks.TextBlock(required=True))))))))), ('people', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('intro', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('people', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.PageChooserBlock()))))), ('featured_pages', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('pages', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('page', wagtail.wagtailcore.blocks.PageChooserBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('sub_text', wagtail.wagtailcore.blocks.CharBlock(max_length=100))))))))), ('sign_up_form_page', wagtail.wagtailcore.blocks.StructBlock((('page', wagtail.wagtailcore.blocks.PageChooserBlock('core.SignUpFormPage')),))), ('logos', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('intro', wagtail.wagtailcore.blocks.CharBlock()), ('logos', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('link_page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link_external', wagtail.wagtailcore.blocks.URLBlock(required=False))))))))))),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='intro',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]