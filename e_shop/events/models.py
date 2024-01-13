from django.db import models
from django.db.models import CASCADE

from e_shop.e_shop_base.models import Profile


class Event(models.Model):

    event_img = models.ImageField(upload_to="event_img")
    title = models.CharField()
    text = models.TextField()
    date = models.DateField()
    link = models.URLField(blank=True, null=True)


class CommentEvent(models.Model):

    comment = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    to_profile = models.ForeignKey(Profile, on_delete=CASCADE)
    to_event = models.ForeignKey(Event, on_delete=CASCADE)

