from django.urls import path


from storesample.views import SampleDetailView,SampleListView
app_name = 'storesample'


urlpatterns = [
    path('samplelist/', SampleListView.as_view(), name='sample-list'),
    path('sample/<int:pk>', SampleDetailView.as_view(), name='sample-detail'),
]

