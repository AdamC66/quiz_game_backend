from django.urls import path, include

from django.conf.urls.static import static
from django.urls import re_path, path
from apps.quiz_user.rest.api import QuizUserViewSet

urlpatterns = [
    path('user/', QuizUserViewSet.as_view()),
]
