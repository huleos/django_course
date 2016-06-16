from django.conf.urls import url
from core.views import NewsletterView

urlpatterns = [
	url(r'^newsletter/$', NewsletterView.as_view(), name='newsletter'),
]