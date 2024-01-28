
from django.urls import path
from .views import upload_content,get_user_media
urlpatterns = [ 
path('upload_content/', upload_content),
path('user_content/', get_user_media),
]