from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^thread/(?P<thread_id>[0-9]+)/$', views.thread, name='thread'),
    url(r'^thread/(?P<thread_id>[0-9]+)/post/(?P<post_id>[0-9]+)/$', views.post, name='post'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
]