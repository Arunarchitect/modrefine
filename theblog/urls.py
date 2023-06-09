from django.urls import path
from . views import HomeView, ArticleDetailView, CreatePostView, UpdatePostView, DeletePostView, LikeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = 'article_detail'),
    path('create_post/', CreatePostView.as_view(), name= 'create_post'),
    path('edit/<int:pk>', UpdatePostView.as_view(), name= 'update_post'),
    path('delete/<int:pk>', DeletePostView.as_view(), name= 'delete_post'),
    path('like/<int:pk>', LikeView, name='like_post'),
]
