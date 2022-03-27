from django.shortcuts import render
from django.utils import timezone
from .models import Post
import sqlite3

from django.contrib.auth.models import User

def post_list(request):

    user_name = User.objects.all()
    print(user_name)


    posts = Post.objects.all()
    last_post_id = len(posts) - 1

    post_id = last_post_id
    post_title = posts[last_post_id].title
    post_text = posts[last_post_id].text
    post_data = posts[last_post_id].created_date


    return render(request, 'blog/post_list.html', {'post_title': post_title, 'post_text': post_text,
                'post_data': post_data, 'post_id': post_id})


def all_post_list(request):
    user_name = User.objects.all()
    print(user_name)

    posts = Post.objects.all()

    for i in range(len(posts)):

        last_post_id = len(posts) - i

        post_id = last_post_id
        post_title = posts[last_post_id].title
        post_text = posts[last_post_id].text
        post_data = posts[last_post_id].created_date

        return render(request, 'blog/all_post_list.html', {'post_title': post_title, 'post_text': post_text,
                                                           'post_data': post_data, 'post_id': post_id})

