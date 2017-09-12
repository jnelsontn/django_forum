from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.views import generic
from .models import *
from .forms import *


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


class ForumCreateReplyView(generic.CreateView):

	model = Post
	context_object_name = 'post'
	template_name = 'thread_post_reply.html'
	fields = ['content']

	def form_valid(self, form):
		thread = get_object_or_404(Thread, slug=self.kwargs['slug'])
		form.instance.thread = thread
		form.instance.user = self.request.user
		return super().form_valid(form)


class ForumPostEditView(generic.UpdateView):

	model = Post
	context_object_name = 'post'
	template_name = 'edit_post.html'
	fields = ['content']

	def form_valid(self, form):
		this_user = self.request.user.id
		post_author = self.object.user.id

		if this_user is not post_author:
			return HttpResponse('Access Denied.')
		return super().form_valid(form)


class ForumPostDeleteView(generic.DeleteView):

	model = Post
	template_name = 'delete_post.html'

	def delete(self, *args, **kwargs):
		self.obj = self.get_object()
		this_user = self.request.user.id
		post_author = self.obj.user.id

		if this_user is not post_author:
			return HttpResponse('Access Denied.')
		return super().delete(self.obj)

	def get_success_url(self):
		obj = self.get_object()
		return reverse('forum:view_thread', kwargs={'slug': obj.thread.slug })


def ForumCreateThreadView(request):

	if request.method == 'POST':
		thread_form = ThreadForm(request.POST)
		thread_post_form = PostForm(request.POST)

		if thread_form.is_valid() and thread_post_form.is_valid():

			new_thread = thread_form.save(commit=False)
			new_thread.user = request.user
			new_thread.save()

			new_post = thread_post_form.save(commit=False)
			new_post.thread = Thread.objects.get(pk=new_thread.id)
			new_post.user = request.user
			new_post.save()

			url = reverse('forum:view_thread', kwargs={'slug': new_thread.slug})
			return HttpResponseRedirect(url)
		else:
			return HttpResponse('Error Submitting Form')
	else:
		create_thread_form = ThreadForm()
		create_post_form = PostForm()

		return render(request, 'thread_create.html', 
			{'create_thread_form': create_thread_form, 
			'create_post_form': create_post_form})


class UserProfileView(generic.DetailView):

	model = User
	context_object_name = 'profile'
	template_name = 'profile_detail.html'


class UserProfileEditView(generic.UpdateView):

	model = User
	context_object_name = 'profile'
	template_name = 'edit_profile.html'
	fields = ['first_name', 'last_name', 'email']

	def get_object(self):
		return get_object_or_404(User, pk=self.request.user.id)

	def form_valid(self, form):
		return HttpResponseRedirect(reverse('forum:view_forum_index'))




