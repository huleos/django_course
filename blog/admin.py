from django.contrib import admin
from blog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
	filter_horizontal = ['categories']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)