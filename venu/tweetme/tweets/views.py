from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, Http404

from .models import Tweet
# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", {})


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {"id": tweet_id}
    status = 200
    try:
        tweet = Tweet.objects.get(id=tweet_id)
        data["content"] = tweet.content
    except:
        data["message"] = "Not Found"
        status = 404

    return JsonResponse(data, status=status)
