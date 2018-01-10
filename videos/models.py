from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager


# Create your models here.
class Video(models.Model):
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title 		= models.CharField(max_length=120)
	slug 		= models.SlugField(unique=True)
	url 		= models.URLField()
	tags 		= TaggableManager(blank=True)
	created_at 	= models.DateTimeField(auto_now_add=True)
	updated_at 	= models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["-created_at", "-updated_at"]

	def __str__(self):
		return self.title


