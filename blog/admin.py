from django.db import models
from django.contrib import admin
from blog.models import Post, Category


def make_published(modeladmin, request, queryset):
	queryset.update(status='published')
make_published.short_description = 'Mark as published'


class PostAdmin(admin.ModelAdmin):
	class Media:
		js = ('//cdn.tinymce.com/4/tinymce.min.js', '/static/js/vendor/tinymce.js')

	list_display = ('title', 'author', 'date_create', 'slug', 'status')
	list_editable = ('author', 'slug', 'status')
	list_filter = ('title', 'date_create', 'categories')
	fieldsets = (
		(None, {
			'fields': ('author',)
		}),
		('Post details',{
			'fields': (('title', 'slug',), 'status', 'body', 'categories',)
		}),
		('Dates',{
			'fields': (('date_create', 'date_update'),)
		})
	)	
	filter_horizontal = ['categories']
	search_fields = ('title', 'body', 'author__email')
	save_on_top = True
	readonly_fields = ('date_create', 'date_update')
	actions = (make_published,)
	ordering = ('-date_create', 'title')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)