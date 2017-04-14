from __future__ import absolute_import, unicode_literals

from django import forms
from django.core.mail import EmailMessage
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.shortcuts import render
from django.utils.functional import cached_property
from django.views.decorators.vary import vary_on_headers

from modelcluster.fields import ParentalKey, ForeignKey
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, InlinePanel,
                                                MultiFieldPanel,
                                                PageChooserPanel,
                                                StreamFieldPanel)
from wagtail.wagtailadmin.utils import send_mail
from wagtail.wagtailcore.blocks import (CharBlock, FieldBlock, ListBlock,
                                        PageChooserBlock, RawHTMLBlock,
                                        RichTextBlock, StreamBlock,
                                        StructBlock, TextBlock, URLBlock)
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.models import (AbstractImage, AbstractRendition,
                                          Image)
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet
from wagtailmarkdown.fields import MarkdownBlock
from .apps import KhanatekCoreAppConfig






# Streamfield blocks and config

class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('left', 'Wrap left'),
        ('right', 'Wrap right'),
        ('half', 'Half width'),
        ('full', 'Full width'),
    ))


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    alignment = ImageFormatChoiceBlock()
    caption = CharBlock()
    attribution = CharBlock(required=False)

    class Meta:
        icon = "image"


class PhotoGridBlock(StructBlock):
    images = ListBlock(ImageChooserBlock())

    class Meta:
        icon = "grip"


class PullQuoteBlock(StructBlock):
    quote = CharBlock(classname="quote title")
    attribution = CharBlock()

    class Meta:
        icon = "openquote"


class PullQuoteImageBlock(StructBlock):
    quote = CharBlock()
    attribution = CharBlock()
    image = ImageChooserBlock(required=False)


class BustoutBlock(StructBlock):
    image = ImageChooserBlock()
    text = RichTextBlock()

    class Meta:
        icon = "pick"


class WideImage(StructBlock):
    image = ImageChooserBlock()

    class Meta:
        icon = "image"


class StatsBlock(StructBlock):
    pass

    class Meta:
        icon = "order"


class StoryBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title")
    h3 = CharBlock(icon="title", classname="title")
    h4 = CharBlock(icon="title", classname="title")
    intro = RichTextBlock(icon="pilcrow")
    paragraph = RichTextBlock(icon="pilcrow")
    aligned_image = ImageBlock(label="Aligned image")
    wide_image = WideImage(label="Wide image")
    bustout = BustoutBlock()
    pullquote = PullQuoteBlock()
    raw_html = RawHTMLBlock(label='Raw HTML', icon="code")
    embed = EmbedBlock(icon="code")
    markdown = MarkdownBlock(icon="code")


# A couple of abstract classes that contain commonly used fields
class ContentBlock(models.Model):
    content = RichTextField()

    panels = [
        FieldPanel('content'),
    ]

    class Meta:
        abstract = True


class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]

    class Meta:
        abstract = True


class ContactFields(models.Model):
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address_1 = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    post_code = models.CharField(max_length=10, blank=True)

    panels = [
        FieldPanel('telephone'),
        FieldPanel('email'),
        FieldPanel('address_1'),
        FieldPanel('address_2'),
        FieldPanel('city'),
        FieldPanel('country'),
        FieldPanel('post_code'),
    ]

    class Meta:
        abstract = True

# Related links
class RelatedLink(LinkFields):
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


# Home Page

class HomePageHero(Orderable, RelatedLink):
    page = ParentalKey('core.HomePage', related_name='hero')
    colour = models.CharField(max_length=255)
    background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    text = models.CharField(
        max_length=255
    )

    panels = RelatedLink.panels + [
        ImageChooserPanel('background'),
        ImageChooserPanel('logo'),
        FieldPanel('colour'),
        FieldPanel('text'),
    ]


class HomePageClient(Orderable, RelatedLink):
    page = ParentalKey('core.HomePage', related_name='clients')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = RelatedLink.panels + [
        ImageChooserPanel('image')
    ]


class HomePage(Page):
    hero_intro_primary = models.TextField(blank=True)
    hero_intro_secondary = models.TextField(blank=True)
    intro_body = RichTextField(blank=True)
    work_title = models.TextField(blank=True)
    project_title = models.TextField(blank=True)
    clients_title = models.TextField(blank=True)
    search_fields = Page.search_fields + [
    	index.SearchField('intro_body'),
    ]

    class Meta:
        verbose_name = "Homepage"

HomePage.content_panels = [
        FieldPanel('title', classname="full title"),
        MultiFieldPanel(
            [
                FieldPanel('hero_intro_primary'),
                FieldPanel('hero_intro_secondary'),
            ],
            heading="Hero intro"
        ),
        InlinePanel('hero', label="Hero"),
        FieldPanel('intro_body'),
        FieldPanel('work_title'),
        FieldPanel('project_title'),
        FieldPanel('clients_title'),
        InlinePanel('clients', label="Clients"),
    ]

    # @property
    # def blog_posts(self):
    #     # Get list of blog pages.
    #     blog_posts = BlogPage.objects.live().public()

    #     # Order by most recent date first
    #     blog_posts = blog_posts.order_by('-date')

    #     return blog_posts
