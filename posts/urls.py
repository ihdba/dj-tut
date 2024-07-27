

from django.urls import path

app_name = 'posts'

from . import views

urlpatterns = [
    path('', views.posts_list, name='list'),
    path('new-post/', views.new_post_view, name='new-post'),
    path('<slug:slug>', views.post_page, name='page'),
]
