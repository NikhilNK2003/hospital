from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('', views.list_blog_posts, name='list_blog_posts'),
    path('category/<str:category_name>/', views.list_blog_posts_by_category, name='list_blog_posts_by_category'),
    path('drafts/', views.list_user_drafts, name='list_user_drafts'),
    path('drafts/category/<str:category_name>/', views.list_user_drafts_category, name='list_user_drafts_category'),
    path('published/', views.list_user_published, name='list_user_published'),
    path('published/category/<str:category_name>/', views.list_user_published_category, name='list_user_published_category'),
]
