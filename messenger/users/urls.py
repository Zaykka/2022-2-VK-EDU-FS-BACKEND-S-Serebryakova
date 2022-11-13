from django.urls import path
from users.views import *


urlpatterns = [
    path('user_info/<int:pk>', UserAPIView.as_view()),
]