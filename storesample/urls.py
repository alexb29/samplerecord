from django.urls import path


from storesample.views import SampleDetailView, SampleListView
from storesample.views import SearchSampleListView, UpdateSample
app_name = 'storesample'


urlpatterns = [
    path('samplelist/', SampleListView.as_view(), name='sample-list'),    
    path('filterlist/', SearchSampleListView.as_view(), name='filtered-list'),
    path('sample/<int:pk>', SampleDetailView.as_view(), name='sample-detail'),
    path('updatesample/<int:pk>', UpdateSample.as_view(), name='sample-update'),
]

