from django.db import models


class Rating(models.Model):
    pic_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField()
    ip_address = models.CharField(max_length=15)


class Comment(models.Model):
    pic_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    ip_address = models.CharField(max_length=15)
