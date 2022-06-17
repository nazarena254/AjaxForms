from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from ajaxapp.views import (
    checkNickName
)
#from .views import index

urlpatterns=[
    path('',views.indexView , name="index"),
    path('post/ajax/friend',views.postFriend, name="post_friend"),
    path('get/ajax/validate/nickname', checkNickName, name = "validate_nickname"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)