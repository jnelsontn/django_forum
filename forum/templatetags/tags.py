from django.contrib.auth.models import User
from django import template
from forum.models import *

register = template.Library()

@register.inclusion_tag('most_recent_threads.html')
def show_most_recent_threads():
	threads = Thread.objects.all().order_by('-id')[:5]
	return {'threads': threads}

@register.inclusion_tag('forum_stats.html')
def display_forum_statistics():
	threads = Thread.objects.all().order_by('id')
	posts = Post.objects.all()
	users = User.objects.all()

	return {
		'threads': threads,
		'posts': posts,
		'users': users
	}