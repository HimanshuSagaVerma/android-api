from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^api-a/', views.api_a1),
	url(r'^api-b/', views.api_b1),
	url(r'^api-c/', views.api_c1),
	url(r'^api-d/', views.api_d1),
	url(r'^api-e/', views.api_e1),
]
