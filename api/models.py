from django.db import models

# Create your models here.

class Register(models.Model):
	username = models.CharField(max_length = 100, null = True)
	mobile = models.CharField(max_length = 15, null = True)
	email = models.CharField(max_length = 80, null = True)
	password = models.CharField(max_length = 80, null = True)

	def __str__(self):
		return str(self.username)

