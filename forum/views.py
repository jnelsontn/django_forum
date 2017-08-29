from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from forum.models import *
from django.core.urlresolvers import reverse

def index(request):
    threads = Thread.objects.all()
    context = {
    	'threads': threads
    }
    return render(request, 'index.html', context)

def thread(request, thread_id):
	thread = get_object_or_404(Thread, pk=thread_id)
	replies = thread.post_set.all()[1:]
	context = {
		'thread': thread,
		'replies': replies
	}
	return render(request, 'thread.html', context)

def post(request, thread_id, post_id):
	thread = get_object_or_404(Thread, pk=thread_id)
	post = thread.post_set.get(pk=post_id)
	context = {
		'post': post
	}
	return render(request, 'post.html', context)

def profile(request, user_id):
	profile = get_object_or_404(User, pk=user_id)
	context = {
		'profile': profile,
	}
	return render(request, 'profile.html', context)