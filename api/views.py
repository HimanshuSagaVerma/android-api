import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
	file_name = "home.html"
	context = {}
	return render(request, file_name, context)

