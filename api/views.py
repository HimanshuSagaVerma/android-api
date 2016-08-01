import json
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.http import HttpResponse
from api.models import api_model
from api.models import api_north, api_south, api_east, api_west, Register
from api.models import api_a, api_b, api_c, api_d, search
# Create your views here.

def android_api_volley(request):
	domain = "http://iwedcast.com/media/"
	l = request.GET.get('location', '')
	all_api = api_model.objects.filter(
		location__icontains=l
	)
	# my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['location'] = i.location
		single_api['image'] = domain + str(i.image)
		single_api['url'] = i.url
		my_array.append(single_api)

	# my_response['details'] = my_array
	my_array = json.dumps(my_array)
	return HttpResponse(my_array)

def android_api(request):
	domain = "http://iwedcast.com/media/"
	l = request.GET.get('location', '')
	all_api = api_model.objects.filter(
		location__icontains=l
	)
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

def android_api1(request):
	domain = "http://iwedcast.com/media/"

	l = request.GET.get('q', '')
	all_api = api_model.objects.filter(
		location__icontains=l
	)
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['location'] = i.location
		single_api['image'] = domain + str(i.image)
		single_api['url'] = i.url
		my_array.append(single_api)

	my_response['details'] = my_array
	context = {
		'myarray': my_array
	}
	return render(request, 'search.html', context)


def index1(request):
    file = "index1.html"
    context = {}
    return render(request, file, context)

def home_page(request):
	file_name = "home.html"
	context = {}
	all_api = api_model.objects.all()
	context['all_api'] = all_api
	return render(request, file_name, context)

def search1(request):
	domain = "http://iwedcast.com/media/"
	l = request.GET.get('location', '')
	all_api = search.objects.filter(
		location__icontains=l
	)
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['location'] = i.location
		single_api['url'] = i.url
		my_array.append(single_api)

	my_response['details'] = my_array
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)

def api_north1(request):
	domain_north = "http://iwedcast.com/media/"
	all_api = api_north.objects.all()
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['title'] = i.title
		single_api['description'] = i.description
		single_api['image'] = domain_north + str(i.image)
		single_api['url'] = i.url
		my_array.append(single_api)

	my_response['details'] = my_array
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)

def api_south1(request):
	domain_north = "iwedcast.com/media/"
	all_api = api_south.objects.all()
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['title'] = i.title
		single_api['description'] = i.description
		single_api['image'] = domain_north + str(i.image)
		single_api['url'] = i.url
		my_array.append(single_api)

	my_response['details'] = my_array
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)

def api_east1(request):
	domain_north = "http://iwedcast.com/media/"
	all_api = api_east.objects.all()
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['title'] = i.title
		single_api['description'] = i.description
		single_api['image'] = domain_north + str(i.image)
		single_api['url'] = i.url
		my_array.append(single_api)

	my_response['details'] = my_array
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)

def api_west1(request):
	domain_west = "http://iwedcast.com/media/"
	all_api = api_west.objects.all()
	my_response = {}
	my_array = []
	for i in all_api:
		single_api = {}
		single_api['title'] = i.title
		single_api['description'] = i.description
		single_api['image'] = domain_north + str(i.image)
		single_api['url'] = i.url
		my_array.append(single_api)

	my_response['details'] = my_array
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)

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
		single_api['url'] = i.url
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
		single_api['url'] = i.url
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
		single_api['url'] = i.url
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
		single_api['url'] = i.url
		my_array.append(single_api)

	my_response['details'] = my_array
	my_response = json.dumps(my_response)
	return HttpResponse(my_response)

@csrf_exempt
def register(request):
	data = request.POST
	username = data.get('username')
	mobile = data.get('mobile')
	email = data.get('email')
	password = data.get('password')

	Register.objects.create(
		username = username,
		mobile = mobile,
		email = email,
		password = password
		)
	return HttpResponse(request.POST)

def register_api(request):
	e = request.GET.get('Email','')


	# New code
	email = request.GET.get('email', '')
	password = request.GET.get('password', '')

	user = Register.objects.filter(email=email, password=password)
	my_response = {}
	my_array = []
	print 'user; ', user
	if user:
		user_detail = {
			'user_found': "True",
			'email': user[0].email,
			'username': user[0].username,
			'password': user[0].password,
		}
	else:
		user_detail = {
			'user_found': "False",
			'email': '',
			'username': '',
			'password': '',
		}
	my_array.append(user_detail)
	my_response['user_detail'] = my_array
#	my_response['user_detail'] = user_detail

	return HttpResponse(json.dumps(my_response))


	# all_api = Register.objects.filter(
	# 	email__icontains = e
	# )
	# my_response = {}
	# my_array = []
	# for i in all_api:
	# 	single_api = {}
	# 	single_api['Email']=i.email
	# 	single_api['Password']=i.password
	# 	my_array.append(single_api)

	# my_response['details'] = my_array
	# my_response = json.dumps(my_response)
	# return HttpResponse(my_response)
