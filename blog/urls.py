from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^posts/$', post_list, name='post_list'),
    url(r'^post/(\d+)', post_detail, name='post_detail'),
    url(r'^posts/create/', create_post, name='create_post'),
    url(r'^posts/edit/(\d+)', edit_post, name='edit_post'),
]