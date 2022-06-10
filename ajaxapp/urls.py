from django.urls import path,include
from . import views
#from .views import index

urlpatterns=[
    path('',views.indexView , name="index"),
    path('post/ajax/friend',views.postFriend, name="post_friend")
]