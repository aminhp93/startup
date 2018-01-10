from django import views
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


def home(request):
	template = 'home.html'
	context = {}
	return render(request, template, context)

class RootAPIView(APIView):
	def get(self, request, format=None):
		return Response({
				"videos": reverse('videos-api:list', request=request, format=format)
			})