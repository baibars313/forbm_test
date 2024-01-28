from django.db import models
from django.contrib.auth.models import User
from authApi.models import ContentGroup


class Content(models.Model):
    PUBLIC = "public"
    PRIVATE = "private"
    GROUP = "group"


    ACCESS_CHOICES = [
        (PUBLIC, "Public"),
        (PRIVATE, "Private"),
        (GROUP, "Group"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.CharField(
        max_length=10, choices=ACCESS_CHOICES, default=PRIVATE
    )
    groups = models.ManyToManyField(ContentGroup, blank=True)
    src = models.FileField(upload_to='uploads/')
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return f"{self.user.username} - {self.content_type}"

