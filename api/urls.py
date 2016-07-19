from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.home_page),
	url(r'^android-api/', views.android_api),
	url(r'^api-north/', views.api_north1),
	url(r'^api-south/', views.api_south1),
	url(r'^api-east/', views.api_east1),
	url(r'^api-west/', views.api_west1),
]
