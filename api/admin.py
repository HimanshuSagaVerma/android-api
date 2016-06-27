from django.contrib import admin
from api.models import api_model
# Register your models here.

class Api_Model(admin.ModelAdmin):
	pass

admin.site.register(api_model, Api_Model)