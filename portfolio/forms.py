from django import forms
from portfolio.models import PortfolioItem


class PortfolioForm(forms.ModelForm):
	class Meta:
		model = PortfolioItem
		fields = ['categories', 'title', 'edit_slug', 'slug', 'image', 'body', 'status']

	title = forms.CharField(
		required=True,
		error_messages={'required': 'Please enter your name'},
		help_text='A valid name, please.',
		widget=forms.TextInput({ 'placeholder': 'Your name'})
		)
	slug = forms.SlugField(required=False)
	edit_slug = forms.BooleanField(required=False, initial=False)

	def clean_slug(self):
		if self.cleaned_data.get('edit_slug'):
			if not self.cleaned_data.get('slug'):
				raise forms.ValidationError('Slug is required!')