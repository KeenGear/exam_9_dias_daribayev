from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, PostDetailView, add_favorite, remove_favorite

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('post_delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/unlike/', remove_favorite, name='remove_favorite'),
    path('post/<int:pk>/like/', add_favorite, name='add_favorite'),
]
