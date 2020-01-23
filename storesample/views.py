from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from django.utils import timezone
from django.urls import reverse_lazy
from django.http import FileResponse
import operator
from functools import reduce
from django.db.models import Q

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
		
		
class SearchSampleListView(SampleListView):
	#paginate_by = 100 
	#model = Sample  # if pagination is desired
	#template_name = 'storesample/samplefilter_list.html'
	
		
	def get_queryset(self):
		print("I am calling the queryset")
		allentry = Sample.objects.all() 
		query = self.request.GET.get('query')
		if query:
			query_list=query.split()
			filteredresults = allentry.filter(
				reduce(operator.or_,
					(Q(composition__icontains=query) for query in query_list)) |
				reduce(operator.or_,
					(Q(owner__icontains=query) for query in query_list)) 
				)
		print("Reusts of the query", filteredresults)
		return filteredresults
					 
				
class UpdateSample(UpdateView): 
	model = Sample
	fields = [
		'owner',
		'instorage',
		'location',
		'temporarylocation'] 
		
	success_url = reverse_lazy('storesample:sample-list')  


