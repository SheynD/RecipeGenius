from django.conf.urls import patterns, include, url
from django.contrib import admin
from foodnetworkapp.views import PostListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foodnetwork.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^post/', include('foodnetworkapp.urls'))
)
