from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

from videos.models import Video


# Create your models here.
class Question(models.Model):
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	video 		= models.ForeignKey(Video)
	question 	= models.TextField(blank=False, null=False)
	answer 		= models.TextField(blank=True)
	tags 		= TaggableManager(blank=True)
	created_at 	= models.DateTimeField(auto_now_add=True)
	updated_at 	= models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["-created_at", "-updated_at"]

	def __str__(self):
		return "Question number {}".format(self.id)
