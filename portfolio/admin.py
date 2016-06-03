from django.db import models
from django.contrib import admin
from portfolio.models import PortfolioItem, Category


def make_published(modeladmin, request, queryset):
	queryset.update(status='published')
make_published.short_description = 'Mark as published'


class PortfolioAdmin(admin.ModelAdmin):
	class Media:
		js = ('//cdn.tinymce.com/4/tinymce.min.js', '/static/js/vendor/tinymce.js')

	list_display = ('title', 'author', 'date_create', 'slug', 'status')
	list_editable = ('author', 'slug', 'status')
	list_filter = ('title', 'date_create')
	fieldsets = (
		(None, {
			'fields': ('author',)
		}),
		('POsrtfolio details',{
			'fields': (('title', 'slug',), 'status', 'body', 'image', 'categories')
		}),
		('Dates',{
			'fields': (('date_create', 'date_update'),)
		})
	)	
	filter_horizontal = ['categories']
	raw_id_fields = ('author',)
	search_fields = ('title', 'body', 'author__email')
	save_on_top = True
	readonly_fields = ('date_create', 'date_update')
	actions = (make_published,)
	ordering = ('-date_create', 'title')


admin.site.register(PortfolioItem, PortfolioAdmin)
admin.site.register(Category)