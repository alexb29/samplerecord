from django.forms import ModelForm
from storesample.models import Sample 


class ArticleForm(ModelForm):
	class Meta:
		model = Sample
		exclude = ['date_added']
