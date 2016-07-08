from django.views.generic import (
	DetailView,
	ListView,
)
from blog.models import Post


class DetailPost(DetailView):
	template_name = 'blog/post.html'
	model = Post
	context_object_name = 'post'


class ListPost(ListView):
	template_name = 'blog/list.html'
	model = Post
	context_object_name = 'posts'
	paginate_by = 1
	ordering = ('-date_create', 'title')
	queryset = Post.objects.all()