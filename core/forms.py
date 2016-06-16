from django import forms


class NewsletterForm(forms.Form):
	name = forms.CharField(required=True)
	email = forms.EmailField(required=True)