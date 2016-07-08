from django.conf.urls import url
from blog.views import (
	DetailPost,
	ListPost,
)

urlpatterns = [
	url(r'^$', ListPost.as_view(), name='blog-list'),
	url(r'^(?P<slug>[-\w]+)/$', DetailPost.as_view(), name='blog-post')
]