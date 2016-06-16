from django import template
from core.forms import NewsletterForm

register = template.Library()


@register.inclusion_tag('core/newsletter_widget.html', takes_context=True)
def newsletter_widget(context):
	form = context.get('form', NewsletterForm())

	return {
		'form': form
	}