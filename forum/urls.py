from django.conf.urls import include, url
from . import views

app_name = 'forum'
urlpatterns = [
    url(r'^$', views.ForumIndexView.as_view(), name='view_forum_index'),
    url(r'^login/$', views.forum_login_user_view, name="login_user"),
    url(r'^logout/$', views.forum_logout_user_view, name="logout_user"),
    url(r'^register_user/$', views.UserProfileRegisterView.as_view(), name='register_user'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.UserProfileView.as_view(), name='view_user_profile'),
    url(r'^editprofile/$', views.UserProfileEditView.as_view(), name='view_edit_profile'),

    url(r'^create_thread/$', views.forum_create_thread_view, name='create_thread'),
    url(r'^(?P<slug>[-\w]*)/$', views.ForumThreadView.as_view(), name='view_thread'),
    url(r'^(?P<slug>[-\w]*)/reply/$', views.ForumCreateReplyView.as_view(), name='reply_thread'),
    url(r'^(?P<thread>[-\w]*)/(?P<slug>[-\w]*)/$', views.ForumPostView.as_view(), name='view_post'),
    url(r'^(?P<thread>[-\w]*)/(?P<slug>[-\w]*)/edit/$', views.ForumPostEditView.as_view(), name='edit_post'),
    url(r'^(?P<thread>[-\w]*)/(?P<slug>[-\w]*)/delete/$', views.ForumPostDeleteView.as_view(), name='delete_post'),
]
