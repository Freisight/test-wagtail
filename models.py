from django.db import models
from wagtail.models import Page
from wagtail.snippets.models import register_snippet


@register_snippet
class Banner(models.Model):
    # Banners for HomePage and CottageCatalog
    pass

    class Meta:
        verbose_name = "Баннеры"


class HomePage(Page):
    subpage_types = ['articles.ArticleCatalog', 'cottages.CottageCatalog', 'news.NewsCatalog', 'review.ReviewCatalog']
    parent_page_types = []
    # main, credit, deal, contacts and banners












