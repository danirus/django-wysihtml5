#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.db.models import permalink
from django.utils.encoding import python_2_unicode_compatible

from wysihtml5.fields import Wysihtml5TextField

class PublicManager(models.Manager):
    """Returns published articles that are not in the future."""
    
    def published(self):
        return self.get_query_set().filter(publish__lte=datetime.now())


@python_2_unicode_compatible
class Article(models.Model):
    """Article, that accepts comments."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique_for_date='publish')
    abstract = models.TextField()
    body = Wysihtml5TextField()
    publish = models.DateTimeField(default=datetime.now)

    objects = PublicManager()

    class Meta:
        db_table = 'demo_articles'
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('articles-article-detail', None, 
                {'year': self.publish.year,
                 'month': int(self.publish.strftime('%m').lower()),
                 'day': self.publish.day,
                 'slug': self.slug})
