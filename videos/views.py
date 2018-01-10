from django.shortcuts import render
from .models import Video


# Create your views here.
def videos_list(request):
	videos_list = Video.objects.all()
	template = 'videos/videos_list.html'
	context = {'videos_list': videos_list}
	return render(request, template, context)