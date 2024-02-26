from django.urls import path
from .views import BlogPostView

urlpatterns=[
    path('BlogSpot/',BlogPostView.as_view(), name= 'blog_list'),
    path('BlogSpot/<int:ID>',BlogPostView.as_view(), name= 'blog_process')

]