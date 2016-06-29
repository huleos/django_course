from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from portfolio.views_api import PortfolioViewSet
from portfolio.views import (
	DetailPortfolio,
	ListPortfolio,
	CreatePortfolio,
	UpdatePortfolio,
	DeletePortfolio,
	PortfolioView,
)


router = DefaultRouter()
router.register('portfolios', PortfolioViewSet)


urlpatterns = [
	url(r'^$', PortfolioView.as_view(), name='portfolio-index'),
	url(r'^create/$', CreatePortfolio.as_view(), name='create-portfolio'),
	url(r'^update/(?P<pk>[\d]+)/$', UpdatePortfolio.as_view(), name='update-portfolio'),
	url(r'^delete/(?P<pk>[\d]+)/$', DeletePortfolio.as_view(), name='delete-portfolio'),
	url(r'^list/$', ListPortfolio.as_view(), name='portfolio-list'),
	url(r'^(?P<slug>[-\w]+)/$', DetailPortfolio.as_view(), name='portfolio-item'),
	url(r'^api/', include(router.urls), name='portfolio-api')
]