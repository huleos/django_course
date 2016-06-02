from django.contrib import admin
from portfolio.models import PortfolioItem, Category


class PortfolioAdmin(admin.ModelAdmin):
	filter_horizontal = ['categories']


admin.site.register(PortfolioItem, PortfolioAdmin)
admin.site.register(Category)