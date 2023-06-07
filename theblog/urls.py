from django.urls import path
from . views import HomeView, ArticleDetailView, CreatePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = 'article_detail'),
    path('create_post/', CreatePostView.as_view(), name= 'create_post'),
]
