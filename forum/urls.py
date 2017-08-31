from django.conf.urls import url
from . import views

app_name = 'forum'
urlpatterns = [
    url(r'^$', views.ForumIndexView.as_view(), name='view_forum_index'),
    url(r'^(?P<slug>[-\w]*)/$', views.ForumThreadView.as_view(), name='view_thread'),
    url(r'^(?P<thread>[-\w]*)/(?P<slug>[-\w]*)/$', views.ForumPostView.as_view(), name='view_post'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.UserProfileView.as_view(), name='view_user_profile'),
]