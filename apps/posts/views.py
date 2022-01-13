# apps/posts/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.posts.models import Author, Category, Post, Tag

# Create your views here.

def index(request):

	# Grab all the posts that has featured as true
	featured_posts = Post.objects.filter(featured=True)

	# Testing
	# print(featured_posts)
	
	context = {
		'object_list': featured_posts
	}

	return render(request, 'index.html', context)


def posts_list(request):
	return render(request, 'posts-list.html')


def post_single(request):
	return render(request, 'post-single.html')