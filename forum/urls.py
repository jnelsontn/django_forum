from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views
import django.contrib.auth.urls

app_name = 'forum'
urlpatterns = [
	url('^', include('django.contrib.auth.urls')),
	# url('^login/', auth_views.login)

	url(r'^$', views.ForumIndexView.as_view(), name='view_forum_index'),
	url(r'^register_user/$', views.UserProfileRegisterView.as_view(), name='register_user'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.UserProfileView.as_view(), name='view_user_profile'),
    url(r'^editprofile/$', views.UserProfileEditView.as_view(), name='view_edit_profile'),

	url(r'^create_thread/$', views.ForumCreateThreadView, name='create_thread'),
    url(r'^(?P<slug>[-\w]*)/$', views.ForumThreadView.as_view(), name='view_thread'),
    url(r'^(?P<slug>[-\w]*)/reply/$', views.ForumCreateReplyView.as_view(), name='reply_thread'),
    url(r'^(?P<thread>[-\w]*)/(?P<slug>[-\w]*)/$', views.ForumPostView.as_view(), name='view_post'),
    url(r'^(?P<thread>[-\w]*)/(?P<slug>[-\w]*)/edit/$', views.ForumPostEditView.as_view(), name='edit_post'),
    url(r'^(?P<thread>[-\w]*)/(?P<slug>[-\w]*)/delete/$', views.ForumPostDeleteView.as_view(), name='delete_post'),

    # from django.contribute.auth.urls:
    # 
	# ^login/$ [name='login']
	# ^logout/$ [name='logout']
	# ^password_change/$ [name='password_change']
	# ^password_change/done/$ [name='password_change_done']
	# ^password_reset/$ [name='password_reset']
	# ^password_reset/done/$ [name='password_reset_done']
	# ^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
	# ^reset/done/$ [name='password_reset_complete']

]