from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .group_api import content_group_list,assign_users_to_group
from .views import  register_user

urlpatterns = [
    # auth urls
    path('register/', register_user, name='register' ),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # group routes
    path('group_list/', content_group_list, name='token_refresh'),
    path('assign-to-group/<int:group_id>/', assign_users_to_group, name='assign users to group')
]

