from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ContentGroup(models.Model):
    users=models.ManyToManyField(User, related_name="group_users")
    creater=models.ForeignKey(User, on_delete=models.CASCADE)
    group_name=models.CharField(max_length=120)
    description=models.TextField()
    creation_date=models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'{self.group_name}-{self.creater.username}'