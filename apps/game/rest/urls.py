from django.urls import path, include

from django.conf.urls.static import static
from django.urls import re_path, path
from apps.game.rest.api import GameBoardViewSet

urlpatterns = [
    re_path(r'^game/(?P<game_code>[\w-]+)/', GameBoardViewSet.as_view()),
    path('game/', GameBoardViewSet.as_view()),
]
