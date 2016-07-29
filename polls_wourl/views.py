import json
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.http import HttpResponse
from polls_wourl.models import api_a, api_b, api_c, api_d, api_e
from polls_wourl.models import api_f, api_g, api_h, api_i, api_j, api_k
# Create your views here.

def api_a1(request):
	domain_north = "http://iwedcast.com/media/"
	all_api = api_a.objects.all()
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['title'] = i.title
		single_api['description'] = i.description
		single_api['image'] = domain_north + str(i.image)
		my_array.append(single_api)

	my_response['details'] = my_array
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)

def api_b1(request):
	domain_north = "http://iwedcast.com/media/"
	all_api = api_b.objects.all()
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['title'] = i.title
		single_api['description'] = i.description
		single_api['image'] = domain_north + str(i.image)
		my_array.append(single_api)

	my_response['details'] = my_array
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)

def api_c1(request):
	domain_north = "http://iwedcast.com/media/"
	all_api = api_c.objects.all()
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['title'] = i.title
		single_api['description'] = i.description
		single_api['image'] = domain_north + str(i.image)
		my_array.append(single_api)

	my_response['details'] = my_array
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)

def api_d1(request):
	domain_north = "http://iwedcast.com/media/"
	all_api = api_d.objects.all()
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['title'] = i.title
		single_api['description'] = i.description
		single_api['image'] = domain_north + str(i.image)
		my_array.append(single_api)

	my_response['details'] = my_array
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)

def api_e1(request):
	domain_north = "http://iwedcast.com/media/"
	all_api = api_e.objects.all()
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['title'] = i.title
		single_api['description'] = i.description
		single_api['image'] = domain_north + str(i.image)
		my_array.append(single_api)

	my_response['details'] = my_array
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)

def api_f1(request):
	domain_north = "http://iwedcast.com/media/"
	all_api = api_f.objects.all()
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['title'] = i.title
		single_api['description'] = i.description
		single_api['image'] = domain_north + str(i.image)
		my_array.append(single_api)

	my_response['details'] = my_array
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)

def api_g1(request):
	domain_north = "http://iwedcast.com/media/"
	all_api = api_g.objects.all()
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['title'] = i.title
		single_api['description'] = i.description
		single_api['image'] = domain_north + str(i.image)
		my_array.append(single_api)

	my_response['details'] = my_array
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)

def api_h1(request):
	domain_north = "http://iwedcast.com/media/"
	all_api = api_h.objects.all()
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['title'] = i.title
		single_api['description'] = i.description
		single_api['image'] = domain_north + str(i.image)
		my_array.append(single_api)

	my_response['details'] = my_array
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)

def api_i1(request):
	domain_north = "http://iwedcast.com/media/"
	all_api = api_i.objects.all()
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['title'] = i.title
		single_api['description'] = i.description
		single_api['image'] = domain_north + str(i.image)
		my_array.append(single_api)

	my_response['details'] = my_array
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)

def api_j1(request):
	domain_north = "http://iwedcast.com/media/"
	all_api = api_j.objects.all()
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['title'] = i.title
		single_api['description'] = i.description
		single_api['image'] = domain_north + str(i.image)
		my_array.append(single_api)

	my_response['details'] = my_array
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)

def api_k1(request):
	domain_north = "http://iwedcast.com/media/"
	all_api = api_k.objects.all()
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['title'] = i.title
		single_api['description'] = i.description
		single_api['image'] = domain_north + str(i.image)
		my_array.append(single_api)

	my_response['details'] = my_array
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)
