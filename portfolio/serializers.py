from rest_framework import serializers
from portfolio.models import PortfolioItem


class PortfolioSerializer(serializers.ModelSerializer):
	class Meta:
		model = PortfolioItem
		fields = ('id', 'author', 'title', 'slug', 'body', 'status')
		read_only_fields = ('slug',)