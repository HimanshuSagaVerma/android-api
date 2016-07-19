import json
from django.shortcuts import render
from django.http import HttpResponse
from api.models import api_model
from api.models import api_north, api_south, api_east, api_west
# Create your views here.

def android_api(request):
	domain = "http://52.36.208.194:8000/media/"
	all_api = api_model.objects.all()
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['location'] = i.location
		single_api['image'] = domain + str(i.image)
		single_api['url'] = i.url
		my_array.append(single_api)

	my_response['details'] = my_array
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)

def home_page(request):
	file_name = "home.html"
	context = {}
	all_api = api_model.objects.all()
	context['all_api'] = all_api
	return render(request, file_name, context)

def api_north1(request):
	domain_north = "http://52.36.208.194:8000/media/"
	all_api = api_north.objects.all()
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

def api_south1(request):
	domain_north = "http://52.36.208.194:8000/media/"
	all_api = api_south.objects.all()
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

def api_east1(request):
	domain_north = "http://52.36.208.194:8000/media/"
	all_api = api_east.objects.all()
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

def api_west1(request):
	domain_west = "http://52.36.208.194:8000/media/"
	all_api = api_west.objects.all()
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
