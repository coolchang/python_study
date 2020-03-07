from django.urls import path

from .views import post_list, post_list_test

urlpatterns = [path("", post_list), path("test/", post_list_test)]

