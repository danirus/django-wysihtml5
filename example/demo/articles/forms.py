#-*- coding: utf-8 -*-

from django.conf import settings
from django.forms import ModelForm
from demo.articles.models import Article
from demo.twitter_bootstrap import Wysihtml5BootstrapWidget

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'slug', 'abstract', 'body')
        widgets = {
            'body': Wysihtml5BootstrapWidget(
                attrs={'rows': 20, 'cols': 80},
                toolbar_settings=settings.WYSIHTML5_BOOTSTRAP_TOOLBAR)
        }
