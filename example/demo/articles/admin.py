from django.contrib import admin
from wysihtml5.admin import AdminWysihtml5TextFieldMixin
from demo.articles.models import Article

class ArticleAdmin(AdminWysihtml5TextFieldMixin, admin.ModelAdmin):
    list_display  = ('title', 'publish')
    list_filter   = ('publish',)
    search_fields = ('title', 'abstract', 'body')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = ((None, 
                  {'fields': ('title', 'slug', 'abstract', 'body', 
                              'publish',)}),)

admin.site.register(Article, ArticleAdmin)
