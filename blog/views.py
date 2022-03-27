from django.shortcuts import render
from django.utils import timezone
from .models import Post
import sqlite3
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User


def post_detail(request):
    posts = Post.objects.all()
    i = 0
    while i != len(posts):
        last_post_id = len(posts)

        post_id = last_post_id - i
        post_title = posts[last_post_id].title
        print(post_title)
        i += 1
        return render(request, 'blog/post_detail.html', {'post_title': post_title})




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
