from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.shortcuts import render


class BlogView(TemplateView):
    template_name = 'blog/list.html'
