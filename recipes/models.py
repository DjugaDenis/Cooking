from django.db import models


class Repices(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='image/')
	text = models.TextField()
	date = models.DateTimeField()

	def __str__(self):
		return self.title

