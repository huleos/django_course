from django.views.generic import TemplateView, FormView
from core.forms import NewsletterForm
from django.core.mail import EmailMultiAlternatives


class HomeView(TemplateView):
	template_name = 'core/index.html'


class NewsletterView(FormView):
	template_name = 'core/newsletter.html'
	form_class = NewsletterForm
	success_url = '/thanks/'

	def form_valid(self, form):
		return super(NewsletterView, self).form_valid(form)