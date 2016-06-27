from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.home_page),
	url(r'^android-api/', views.android_api),
]