from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'blog'

urlpatterns = [
    path('',views.index,name='index'),
    path('blog/',views.blog_index,name='blog_index'),
    path('contact/',views.contact,name='contact'),
    path('blog/<int:pk>/', views.blog_details, name='blog_details'),
    path('blog/category/',views.blog_category,name='blog_category'),
    path('blog/list/',views.blog_list,name='blog_list'),
    path('blog/comment/', views.blog_comment, name='blog_comment')

]

