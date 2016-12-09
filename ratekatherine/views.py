from django.http import HttpResponse
from django.shortcuts import render

from ratekatherine.models import Rating, Comment


def add_rating(request):
    ip_address = request.META['REMOTE_ADDR']
    rating = request.POST['rating']
    pic_id = request.POST['pic_id']

    existing_rating_query = Rating.objects.filter(pic_id=pic_id, ip_address=ip_address)
    if existing_rating_query:
        rating = existing_rating_query[0]
        rating.rating = request.POST['rating']
        rating.save()
    else:
        rating = Rating(pic_id=pic_id, rating=rating, ip_address=ip_address)
        rating.save()

    return HttpResponse()


def add_comment(request):
    ip_address = request.META['REMOTE_ADDR']
    pic_id = request.POST['pic_id']
    comment = Comment(text=request.POST['text'], pic_id=pic_id, ip_address=ip_address)
    comment.save()

    return HttpResponse()


def get_comments(request):
    template = 'comments.html'
    comments_for_image = Comment.objects.filter(pic_id=request.POST["pic_id"]).order_by('-id')[:100]
    return render(request, template, {"latest_comments": comments_for_image})


def home(request):
    template = 'home.html'

    return render(request, template, {})
