from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render


class PortfolioView(TemplateView):
    template_name = 'portfolio/portfolio-items.html'
