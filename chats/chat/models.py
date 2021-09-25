from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Message(models.Model):
	sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
	content = models.TextField()
	translated = models.TextField()

	def __str__(self):
		return self.content

	def get_absolute_url(self):
	    return reverse('messages-home')

class Language(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	language = models.CharField(max_length=300)

	def get_absolute_url(self):
	    return reverse('messages-home')
























