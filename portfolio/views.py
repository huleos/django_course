from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
	DetailView, 
	ListView,
	CreateView,
	UpdateView,
	DeleteView,
)
from portfolio.models import PortfolioItem


class DetailPortfolio(DetailView):
	template_name = 'portfolio/item.html'
	model = PortfolioItem
	context_object_name = 'portfolio'


class ListPortfolio(ListView):
	template_name = 'portfolio/portfolio-items.html'
	model = PortfolioItem
	context_object_name = 'portfolios'
	paginate_by = 1
	ordering = ('-date_create', 'title')
	queryset = PortfolioItem.objects.all()


class CreatePortfolio(CreateView):
	template_name = 'portfolio/create-portfolio.html'
	model = PortfolioItem
	fields = ['title', 'status', 'body', 'image', 'categories',]


class UpdatePortfolio(UpdateView):
	template_name = 'portfolio/create-portfolio.html'
	model = PortfolioItem
	fields = ['title', 'status', 'body', 'image', 'categories',]


class DeletePortfolio(DeleteView):
	template_name = 'portfolio/delete-portfolio.html'
	model = PortfolioItem
	context_object_name = 'portfolio'
	success_url = reverse_lazy('portfolio-list')