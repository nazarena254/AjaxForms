from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from .views import index

urlpatterns=[
    path('',views.indexView , name="index"),
    path('post/ajax/friend',views.postFriend, name="post_friend")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)