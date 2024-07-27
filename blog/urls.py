from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('',views.index),
    path('blog/',views.blog_index,name='blog_index'),
    path('contact/',views.contact,name='contact'),
    path('blog/<int:pk>/', views.blog_details, name='blog_details'),
    path('blog/category/',views.blog_category,name='blog_category'),
    path('blog/list/',views.blog_list,name='blog_list'),

    

]


    # path('', views.post_list, name='post_list'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new/', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # path('notifications/', views.notification_list, name='notification_list'),