from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .forms import FriendForm
from .models import Friend
from django.core import serializers

#When a client requests for a resource, a HttpRequest object is created and 
# correspond view function is called that returns HttpResponse object

# Create your views here.
# def index(request):
#     return HttpResponse('Hello there')

def indexView(request):
    form = FriendForm
    friends = Friend.objects.all()
    return render(request, "index.html",{"form":form,"friends":friends})

def postFriend(request):
     # request should be ajax and method should be POST
    if request.is_ajax and request.method=="POST":
        # get the form data
        form=FriendForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid:
            instance=form.save()
            # serialize in new friend object in json
            ser_instance=serializers.serialize('json',[instance,])
            # send to client side.
            return JsonResponse({"instance":ser_instance},status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error":form.errors}, status=400) 
    # some error occured
    return JsonResponse({"error": ""}, status=400)


def checkNickName(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        nick_name = request.GET.get("nick_name", None)
        # check for the nick name in the database.
        if Friend.objects.filter(nick_name = nick_name).exists():
            # if nick_name found return not valid new friend
            return JsonResponse({"valid":False}, status = 200)
        else:
            # if nick_name not found, then user can create a new friend.
            return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({}, status = 400)




