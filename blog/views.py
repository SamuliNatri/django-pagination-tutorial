from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView
from django.core.paginator import Paginator
from blog.models import Post

class BlogView(ListView):
    model = Post
    paginate_by = 5
    # template_name = 'blog/index.html'
    template_name = 'blog/blue_theme.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post


def index2(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,
                  'blog/index2.html',
                  {'posts': posts})