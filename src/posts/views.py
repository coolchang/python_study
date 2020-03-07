from django.shortcuts import render

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    potatos = {"post_lists": posts}
    return render(request, "posts/post_list.html", potatos)


def post_list_test(request):
    posts = Post.objects.all()
    potatos = {"post_lists": posts}
    return render(request, "post_list_test.html", potatos)
