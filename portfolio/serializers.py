from rest_framework import serializers
from portfolio.models import PortfolioItem


class PortfolioSerializer(serializers.ModelSerializer):
	url = serializers.URLField(source='get_absolute_url')

	class Meta:
		model = PortfolioItem
		fields = ('id', 'author', 'title', 'slug', 'body', 'status', 'url')
		read_only_fields = ('slug',)