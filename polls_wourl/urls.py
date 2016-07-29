from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^api-a/', views.api_a1),
	url(r'^api-b/', views.api_b1),
	url(r'^api-c/', views.api_c1),
	url(r'^api-d/', views.api_d1),
	url(r'^api-e/', views.api_e1),
	url(r'^api-f/', views.api_f1),
	url(r'^api-g/', views.api_g1),
	url(r'^api-h/', views.api_h1),
	url(r'^api-i/', views.api_i1),
	url(r'^api-j/', views.api_j1),
	url(r'^api-k/', views.api_k1),
]
