from . import views
from django.urls import path


urlpatterns = [
     path('', views.PostList.as_view(), name='blog'),
     path('add_post/', views.PostCreateOrUpdateView.as_view(), name='add_post'),
     path('post/edit/<int:pk>/', views.PostCreateOrUpdateView.as_view(), name='edit_post'),
     path('post/<int:pk>/delete/', views.post_delete_view, name='post_delete'),
     path('blog/<slug:slug>/', views.post_detail.as_view(), name='post_detail'),
     path('blog/<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
     path('blog/<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
     path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]