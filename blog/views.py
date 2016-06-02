from django.views.generic import TemplateView, DetailView
from blog.models import Post


class BlogView(TemplateView):
	template_name = 'blog/list.html'


class DetailPost(DetailView):
	template_name = 'blog/post.html'
	model = Post
	context_object_name = 'post'