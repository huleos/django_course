from django.conf.urls import url
from blog.views import BlogView, DetailPost

urlpatterns = [
	url(r'^$', BlogView.as_view(), name='blog-list'),
	url(r'^(?P<slug>[-\w]+)/$', DetailPost.as_view(), name='blog-post')
]