from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone
from django.http import FileResponse


# Create your views here.
from storesample.models import Sample

class SampleDetailView(DetailView):
	
	template_name = 'storesample/sample_detail.html'
	model = Sample
	
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		try:
			mysample=self.object.samplecif_set.first()
			print("mysample",mysample.ciffiles.path)
			with open(mysample.ciffiles.path, 'r') as myfile:
				mycif = myfile.read() 
				mycif=mycif.replace('\n','<br>')
		except:
			mycif="<p> <span> There are no cif files associated with this object </span> </p>"       
		context['mycif'] = mycif
		return context


class SampleListView(ListView):
	
	model = Sample
	paginate_by = 100  # if pagination is desired
	template_name = 'storesample/sample_list.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context
