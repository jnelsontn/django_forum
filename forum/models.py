from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Thread(models.Model):
	user = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True)
	subject = models.CharField(max_length=255)

	def __str__(self):
		return self.subject + ' by ' + str(self.user)

class Post(models.Model):
	thread = models.ForeignKey(Thread)
	user = models.ForeignKey(User)
	content = models.CharField(max_length=1000)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return 'thread_id: ' + str(self.thread.id) + ' reply by ' + str(self.user) + '. post_id: ' + str(self.id)

