from django.contrib import admin
from polls_wourl.models import api_a, api_b, api_c, api_d, api_e

# Register your models here.

class Api_a1_Model(admin.ModelAdmin):
	pass

admin.site.register(api_a, Api_a1_Model)


class Api_b1_Model(admin.ModelAdmin):
	pass

admin.site.register(api_b, Api_b1_Model)


class Api_c1_Model(admin.ModelAdmin):
	pass

admin.site.register(api_c, Api_c1_Model)


class Api_d1_Model(admin.ModelAdmin):
	pass

admin.site.register(api_d, Api_d1_Model)


class Api_e1_Model(admin.ModelAdmin):
	pass

admin.site.register(api_e, Api_e1_Model)
