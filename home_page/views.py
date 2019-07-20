from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post,Games,Comment


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home_page/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'home_page/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by =4

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['games'] = Games.objects.all()
        return context


class NewsListView(ListView):
    model = Post
    template_name = 'home_page/news.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by =12


# def product_detail_view(request,pk=None,*args,**kwargs):
#     instance = Product.objects.get(pk=pk)
#     # instance = get_object_or_404(pk=pk)
#     context = {
#         'object' : instance
#     }
#     return render(request, 'myproject/detail2.html',context)

# @permission_required('Post.can_add')

def PostDetailView(request,pk,*args,**kwargs):
    post =get_object_or_404(Post,pk=pk)
    template_name = 'home_page/post.html'

    comments = Comment.objects.filter(post=post,reply=None).order_by('-id')
    is_liked = False
    if request.method == 'POST':
        comment_form =CommentForm(request.POST or None)
        if comment_form.is_valid():
            content =request.POST.get('content')
            reply_id=request.POST.get('comment_id')
            comment_qs=None
            if reply_id:
                comment_qs= Comment.objects.get(pk=reply_id)

            comment =Comment.objects.create(post=post,user=request.user,content=content , reply=comment_qs)
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()



    context = {
            'object':post,
            'comments':comments,
            'is_liked':is_liked,
            'comment_form':comment_form,
            'posts':Post.objects.filter(title__contains='')[:2]
        }
    return render(request,template_name, context)




class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
