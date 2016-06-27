from django.db import models

# Create your models here.

class api_model(models.Model):
	location = models.CharField(max_length = 200, null = True)
	image = models.ImageField(upload_to = '/my-media')

	def __str__(self):
		return str(self.location)