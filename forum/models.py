from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
import random


def gen_slug(content, uid=None):
    random_number = str(random.randint(1000, 20000))
    if uid:
        return random_number + '-' + content[:20] + '-' + str(uid)
    else:
        return random_number + '-' + content[:35]


class Thread(models.Model):
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=255)
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return self.subject + ' by ' + str(self.user)

    def save(self):
        if not self.slug:
            self.slug = slugify(gen_slug(self.subject))
        super().save()

    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse('forum:view_thread', kwargs=kwargs)


class Post(models.Model):
    thread = models.ForeignKey(Thread)
    user = models.ForeignKey(User)
    content = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='', blank=True)

    edited = models.BooleanField(default=False)
    edited_date = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return 'thread_id: ' + str(self.thread.id) + ' by ' + str(self.user) + '. post_id: ' + str(self.id)

    def save(self):
        super().save()
        if not self.slug:
            self.slug = slugify(gen_slug(self.content))
        super().save()

    def get_absolute_url(self):
        kwargs = {'thread': self.thread.slug, 'slug': self.slug}
        return reverse('forum:view_post', kwargs=kwargs)
