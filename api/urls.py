from . import views
from django.conf.urls import url

urlpatterns = [
	url('^register/$', views.register, name="register"),
	url(r'^$', views.home_page),
	url(r'^home/', views.index1),
	url('^register-api/', views.register_api),
	url(r'^android-api/', views.android_api),
	url(r'^android-api-volley/', views.android_api_volley),
	url(r'^android-api1/', views.android_api1),
]
