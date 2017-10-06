from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .forms import *
from django.contrib.auth.models import User

# Functions
def forum_create_thread_view(request):
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


def forum_login_user_view(request):

    login_form = LoginForm()

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('forum:view_forum_index'))
        else:
            return render(request, 'login.html', {
                'form': login_form,
                'incorrect': 'Login Incorrect',
            })

    return render(request, 'login.html', {'form': login_form})


def forum_logout_user_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('forum:view_forum_index'))


# Class-based views
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

    def get_success_url(self):
        return reverse('forum:view_thread', kwargs={'slug': self.object.thread.slug})


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
        self.object.edited = True
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('forum:view_thread', kwargs={'slug': self.object.thread.slug})


class ForumPostDeleteView(generic.UpdateView):
    model = Post
    template_name = 'delete_post.html'
    fields = []

    def form_valid(self, form):
        this_user = self.request.user.id
        post_author = self.object.user.id

        if this_user is not post_author:
            return HttpResponse('Access Denied.')
        self.object.content = 'Post Removed by {}'.format(self.object.user)
        self.object.deleted = True
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('forum:view_thread', kwargs={'slug': self.object.thread.slug})


class UserProfileRegisterView(generic.CreateView):
    model = User
    template_name = 'register_user.html'
    fields = ['username', 'email', 'password', 'first_name', 'last_name', ]

    def get_success_url(self):
        return reverse('forum:view_forum_index')


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
