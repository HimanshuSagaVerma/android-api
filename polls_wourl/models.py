from django.db import models

# Create your models here.

class api_a(models.Model):
	title = models.CharField(max_length = 200, null = True)
	image = models.ImageField(upload_to = 'woa')
	description = models.TextField()

	def __str__(self):
		return str(self.title)


class api_b(models.Model):
	title = models.CharField(max_length = 200, null = True)
	image = models.ImageField(upload_to = 'wob')
	description = models.TextField()

	def __str__(self):
		return str(self.title)


class api_c(models.Model):
	title = models.CharField(max_length = 200, null = True)
	image = models.ImageField(upload_to = 'woc')
	description = models.TextField()

	def __str__(self):
		return str(self.title)


class api_d(models.Model):
	title = models.CharField(max_length = 200, null = True)
	image = models.ImageField(upload_to = 'wod')
	description = models.TextField()

	def __str__(self):
		return str(self.title)


class api_e(models.Model):
	title = models.CharField(max_length = 200, null = True)
	image = models.ImageField(upload_to = 'woe')
	description = models.TextField()

	def __str__(self):
		return str(self.title)


class api_f(models.Model):
	title = models.CharField(max_length = 200, null = True)
	image = models.ImageField(upload_to = 'wof')
	description = models.TextField()

	def __str__(self):
		return str(self.title)


class api_g(models.Model):
	title = models.CharField(max_length = 200, null = True)
	image = models.ImageField(upload_to = 'wog')
	description = models.TextField()

	def __str__(self):
		return str(self.title)


class api_h(models.Model):
	title = models.CharField(max_length = 200, null = True)
	image = models.ImageField(upload_to = 'woh')
	description = models.TextField()

	def __str__(self):
		return str(self.title)


class api_i(models.Model):
	title = models.CharField(max_length = 200, null = True)
	image = models.ImageField(upload_to = 'woi')
	description = models.TextField()

	def __str__(self):
		return str(self.title)


class api_j(models.Model):
	title = models.CharField(max_length = 200, null = True)
	image = models.ImageField(upload_to = 'woj')
	description = models.TextField()

	def __str__(self):
		return str(self.title)


class api_k(models.Model):
	title = models.CharField(max_length = 200, null = True)
	image = models.ImageField(upload_to = 'wok')
	description = models.TextField()

	def __str__(self):
		return str(self.title)

