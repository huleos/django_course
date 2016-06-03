from __future__ import unicode_literals
from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse


STATUSES = (
	('draft', 'Draft'),
	('published', 'Published'),
	('deleted', 'Deleted')
)


class PortfolioItem(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True)
	categories = models.ManyToManyField('Category')
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=300, blank=True, default='')
	image = models.ImageField(upload_to='portfolio/')
	body = models.TextField()
	status = models.CharField(max_length=50, default='draft', choices=STATUSES)
	date_create = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title

	def save(self):
		if self.id is None:
			self.slug = slugify(self.title)
		return super(PortfolioItem, self).save()

	def get_absolute_url(self):
		return reverse('portfolio-item', kwargs={'slug': self.slug})


class Category(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name