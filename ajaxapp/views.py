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






