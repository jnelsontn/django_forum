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

class ForumCreateThreadView(generic.CreateView):
	model = Thread
	context_object_name = 'thread'
	template_name = 'thread_create.html'
	fields = ['subject']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(ForumCreateThreadView, self).form_valid(form)

class ForumCreateReplyView(generic.CreateView):
	model = Post
	context_object_name = 'post'
	template_name = 'thread_post_reply.html'
	fields = ['content']

	def form_valid(self, form):
		thread = get_object_or_404(Thread, slug=self.kwargs['slug'])
		form.instance.thread = thread
		form.instance.user = self.request.user
		return super(ForumCreateReplyView, self).form_valid(form)





