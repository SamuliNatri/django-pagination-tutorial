from django.urls import path
from blog.views import PostDetailView, BlogView
from blog.views import index2

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('index2/', index2, name='index2'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
