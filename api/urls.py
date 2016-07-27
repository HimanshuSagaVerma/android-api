from . import views
from django.conf.urls import url

urlpatterns = [
	url('^register/$', views.register, name="register"),
	url(r'^$', views.home_page),
	url(r'^home/', views.index1),
	url('^register-api/', views.register_api),
	url(r'^android-api/', views.android_api),
	url(r'^api-north/', views.api_north1),
	url(r'^api-south/', views.api_south1),
	url(r'^api-east/', views.api_east1),
	url(r'^api-west/', views.api_west1),
	url(r'^api-a/', views.api_a1),
	url(r'^api-b/', views.api_b1),
	url(r'^api-c/', views.api_c1),
	url(r'^api-d/', views.api_d1),
	url(r'^api-search/', views.search),
]
