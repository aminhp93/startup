from django.conf.urls import url

from videos.api import views

urlpatterns = [
	url(r'^$', views.videos_list, name='list'),
	# url(r'^create/$', views.PostCreateAPIView.as_view(), name='create'),
	# url(r'^(?P<slug>[\w-]+)/$', views.PostDetailAPIView.as_view(), name='detail'),
	# url(r'^(?P<slug>[\w-]+)/update/$', views.PostUpdateAPIView.as_view(), name='update'),
	# url(r'^(?P<slug>[\w-]+)/delete/$', views.PostDeleteAPIView.as_view(), name='delete'),
]