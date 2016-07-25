from . import views
from django.conf.urls import url

urlpatterns = [
	url('^register/$', views.register, name="register"),
	url(r'^$', views.home_page),
	url('^register-api/', views.register_api),
	url(r'^android-api/', views.android_api),
	url(r'^api-north/', views.api_north1),
	url(r'^api-south/', views.api_south1),
	url(r'^api-east/', views.api_east1),
	url(r'^api-west/', views.api_west1),
]
