from django.conf.urls import url
from portfolio.views import PortfolioView, DetailPortfolio

urlpatterns = [
	url(r'^$', PortfolioView.as_view(), name='portfolio-list'),
	url(r'^(?P<slug>[-\w]+)/$', DetailPortfolio.as_view(), name='portfolio-item')
]