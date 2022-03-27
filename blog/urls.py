from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('/all_posts', views.all_post_list, name='all_post_list'),
]