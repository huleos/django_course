from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
	DetailView, 
	ListView,
	CreateView,
	UpdateView,
	DeleteView,
	TemplateView,
)
from portfolio.models import PortfolioItem
from blog.models import Post
from django.db.models import Q
from portfolio.forms import PortfolioForm


class PortfolioView(TemplateView):
	template_name = 'portfolio/index.html'

	def get_context_data(self, **kwargs):
		context = super(PortfolioView, self).get_context_data(**kwargs)
		context['posts'] = Post.objects.all()[:3]
		context['portfolios'] = PortfolioItem.objects.filter(Q(status='draft') | Q(status='published'))[:3]
		return context


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
	form_class = PortfolioForm


class UpdatePortfolio(UpdateView):
	template_name = 'portfolio/create-portfolio.html'
	model = PortfolioItem
	fields = ['title', 'status', 'body', 'image', 'categories',]


class DeletePortfolio(DeleteView):
	template_name = 'portfolio/delete-portfolio.html'
	model = PortfolioItem
	context_object_name = 'portfolio'
	success_url = reverse_lazy('portfolio-list')