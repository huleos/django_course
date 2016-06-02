from django.views.generic import TemplateView, DetailView
from portfolio.models import PortfolioItem


class PortfolioView(TemplateView):
    template_name = 'portfolio/portfolio-items.html'


class DetailPortfolio(DetailView):
	template_name = 'portfolio/item.html'
	model = PortfolioItem
	context_object_name = 'portfolio'
