from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from .models import Post, Reviews, Hashtag
from django import template
from django.contrib.auth.models import User
import json

# Create your views here.

def hashtaging(request, id):
    hashtag = get_object_or_404(Hashtag, pk=id)
    id = hashtag.id
    posts = Post.objects.filter(hashtags=hashtag)
    return render(request, "partHome.html", {"posts":posts, "hashtag":hashtag})

def partHome(request):
    posts = Post.objects.all
    return render(request,"partHome.html", {"posts":posts})
#해시태그 붙이기 필요
def createPart(request):
    if request.method == "POST":
        isPost = Post.objects.filter(url=request.POST["url"])
        if isPost.count() > 0:
            if request.POST["url"] == isPost[0].url:
                review = Reviews()
                review.post = isPost[0]
                review.reviews_textfield = request.POST["textfield"]
                review.save()
                isPost[0].hashtagBox = isPost[0].hashtagBox + "".join(request.POST["hashtagBox"])
                isPost[0].save()
                hashtagBox = isPost[0].hashtagBox
                hashtagBox_words = hashtagBox.split()
                for word in hashtagBox_words:
                    if word[0] == "#":
                        tag = Hashtag.objects.get_or_create(content=word)
                        isPost[0].hashtags.add(tag[0])
        else:
            post = Post()
            post.url = request.POST["url"]
            post.hashtagBox = request.POST["hashtagBox"]
            review = Reviews()
            review.post = post
            review.reviews_textfield = request.POST["textfield"]
            post.save()
            review.save()
            hashtagBox = request.POST["hashtagBox"]
            hashtagBox_words = hashtagBox.split()
            for word in hashtagBox_words:
                if word[0] == "#":
                    tag = Hashtag.objects.get_or_create(content=word)
                    post.hashtags.add(tag[0])
        return redirect("videopage:partHome")
    elif request.method == "GET":
        return render(request, "newPartHome.html")


def partHomeDetail(request, id):
    post = get_object_or_404(Post, pk=id)
    reviews = Reviews.objects.filter(post_id=id)
    return render(request, "partHomeDetail.html", {"post":post, "reviews":reviews })

def reviewsDelete(request, id):
    reviews = get_object_or_404(Reviews, pk=id)
    reviews.delete()
    return redirect("videopage:partHome")