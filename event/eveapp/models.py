from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
	event_title = models.CharField(max_length=150)
	location = models.CharField(max_length=150)
	event_date = models.DateTimeField(default=timezone.now)
	image = models.ImageField(upload_to='images/')
	is_liked = models.BooleanField(null=True)

	

	def __str__(self):
		return self.event_title
	


