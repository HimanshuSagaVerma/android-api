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
	url(r'^api-a-volley/', views.api_a1_volley),
	url(r'^api-b-volley/', views.api_b1_volley),
	url(r'^api-c-volley/', views.api_c1_volley),
	url(r'^api-d-volley/', views.api_d1_volley),
	url(r'^api-e-volley/', views.api_e1_volley),
	url(r'^api-f-volley/', views.api_f1_volley),
	url(r'^api-g-volley/', views.api_g1_volley),
	url(r'^api-h-volley/', views.api_h1_volley),
	url(r'^api-i-volley/', views.api_i1_volley),
	url(r'^api-j-volley/', views.api_j1_volley),
	url(r'^api-k-volley/', views.api_k1_volley),
]
