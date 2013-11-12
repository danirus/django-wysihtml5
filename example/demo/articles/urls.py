from django.core.urlresolvers import reverse
from django.conf.urls import patterns, url
from django.views.generic import (ListView, DateDetailView, 
                                  CreateView, UpdateView)

from demo.articles.forms import ArticleForm
from demo.articles.models import Article


urlpatterns = patterns(
    '',
    url(r'^$', 
        ListView.as_view(queryset=Article.objects.published()),
        name='articles-index'),

    url(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<day>\d{1,2})/'
        r'(?P<slug>[-\w]+)/$',
        DateDetailView.as_view(model=Article, date_field="publish", 
                               month_format="%m"), 
        name='articles-article-detail'),

    url(r'^new/$', 
        CreateView.as_view(success_url='/articles/',
                           form_class=ArticleForm,
                           template_name='articles/article_new.html'),
        name='articles-article-new'),
)
