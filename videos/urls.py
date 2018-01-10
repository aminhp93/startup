from django.conf.urls import url
from .views import (
        videos_list
    )

urlpatterns = [
    url(r'^$', videos_list, name='list'),
    # url(r'^create/$', PostCreateView.as_view(), name='create'),
    # url(r'^(?P<slug>[-\w]+)/$', post_detail, name='detail'),
    # url(r'^(?P<slug>[-\w]+)/update/$', PostUpdateView.as_view(), name='update'),
    # url(r'^(?P<slug>[-\w]+)/delete/$', PostDeleteView.as_view(), name='delete'),

]
