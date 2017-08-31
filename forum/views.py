from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.views import generic
from forum.models import *

class ForumIndexView(generic.ListView):
	model = Thread
	context_object_name = 'threads'
	template_name = 'index.html'

class ForumThreadView(generic.DetailView):
	model = Thread
	context_object_name = 'thread'
	template_name = 'thread_detail.html'

class ForumPostView(generic.DetailView):
	model = Post
	context_object_name = 'post'
	template_name = 'post_detail.html'

class UserProfileView(generic.DetailView):
	model = User
	context_object_name = 'profile'
	template_name = 'profile_detail.html'