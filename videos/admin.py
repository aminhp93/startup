from django.contrib import admin

# Register your models here.
from .models import Video

class VideoAdmin(admin.ModelAdmin):
	 prepopulated_fields = {"slug": ("title",)}

admin.site.register(Video, VideoAdmin)