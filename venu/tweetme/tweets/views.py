from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, Http404

from .models import Tweet
# Create your views here.


def tweet_list_view(request, *args, **kwargs):
    all_tweets = Tweet.objects.all()
    tweets_list = [{"id": tweet.id, "content": tweet.content, "likes": 0}
                   for tweet in all_tweets]
    data = {
        "response": tweets_list
    }

    return JsonResponse(data)


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
