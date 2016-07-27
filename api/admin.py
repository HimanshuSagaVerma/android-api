from django.contrib import admin
from api.models import api_model, api_north, api_south, api_east, api_west, Register
from api.models import api_a, api_b, api_c, api_d
# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
	pass

admin.site.register(Register, RegisterAdmin)

class Api_Model(admin.ModelAdmin):
	pass

admin.site.register(api_model, Api_Model)


class Api_1_Model(admin.ModelAdmin):
	pass

admin.site.register(api_north, Api_1_Model)


class Api_2_Model(admin.ModelAdmin):
	pass

admin.site.register(api_south, Api_2_Model)


class Api_3_Model(admin.ModelAdmin):
	pass

admin.site.register(api_east, Api_3_Model)


class Api_4_Model(admin.ModelAdmin):
	pass

admin.site.register(api_west, Api_4_Model)


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
