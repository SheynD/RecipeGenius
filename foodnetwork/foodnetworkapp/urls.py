from django.conf.urls import patterns, url
from views import PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    url(r'^add/$', PostCreateView.as_view(), name='create')
    url(r'^(?P<pk>[\w\d]+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[\w\d]+)/edit/$', PostUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[\w\d]+)/delete/$', PostDeleteView.as_view(), name='delete'),
]
