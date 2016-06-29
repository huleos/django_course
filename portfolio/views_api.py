from rest_framework import viewsets
from portfolio.serializers import PortfolioSerializer
from portfolio.models import PortfolioItem


class PortfolioViewSet(viewsets.ModelViewSet):
	serializer_class = PortfolioSerializer
	queryset = PortfolioItem.objects.all()