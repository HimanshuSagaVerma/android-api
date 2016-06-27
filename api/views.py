import json
from django.shortcuts import render
from django.http import HttpResponse
from api.models import api_model
# Create your views here.

def android_api(request):
	domain = "http://127.0.0.1:8000/media/"
	all_api = api_model.objects.all()
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['location'] = i.location
		single_api['image'] = domain + str(i.image)
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