from django.db import models

# Create your models here.

class Register(models.Model):
	username = models.CharField(max_length = 100, null = True)
	mobile = models.CharField(max_length = 15, null = True)
	email = models.CharField(max_length = 80, null = True)
	password = models.CharField(max_length = 80, null = True)

	def __str__(self):
		return str(self.username)

class api_model(models.Model):
	location = models.CharField(max_length = 200, null = True)
	image = models.ImageField(upload_to = 'my-media')
	url = models.CharField(max_length = 2000, null = True)

	def __str__(self):
		return str(self.location)


class api_north(models.Model):
	title = models.CharField(max_length = 200, null = True)
	image = models.ImageField(upload_to = 'north')
	description = models.TextField()

	def __str__(self):
		return str(self.title)


class api_south(models.Model):
	title = models.CharField(max_length = 200, null = True)
	image = models.ImageField(upload_to = 'south')
	description = models.TextField()

	def __str__(self):
		return str(self.title)


class api_east(models.Model):
	title = models.CharField(max_length = 200, null = True)
	image = models.ImageField(upload_to = 'east')
	description = models.TextField()

	def __str__(self):
		return str(self.title)


class api_west(models.Model):
	title = models.CharField(max_length = 200, null = True)
	image = models.ImageField(upload_to = 'west')
	description = models.TextField()

	def __str__(self):
		return str(self.title)


# Some comment
