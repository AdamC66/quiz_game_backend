from rest_framework import generics, permissions
from rest_framework.response import Response
from apps.quiz_user.models import QuizUser
from apps.game.actions import create_game
from apps.game.models import GameBoard
from apps.game.rest.serializers import  GameBoardSerializer, GameBoardListSerializer
from django.contrib.auth import login
from rest_framework import permissions

class GameBoardViewSet(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    lookup_field = "code"
    lookup_url_kwarg = "game_code"
    def get_queryset(self):
        queryset = GameBoard.objects.all().filter(user=self.request.user)
        return queryset
    
    def retrieve(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer = GameBoardSerializer(instance=instance)
        return Response(serializer.data)
    def list(self, request, *args, **kwargs):
        queryset=self.get_queryset()
        serializer = GameBoardListSerializer(queryset, many=True)
        return Response(serializer.data)
    def get(self, request, *args, **kwargs):
        if self.lookup_url_kwarg in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
        
    # def get(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = GameBoardListSerializer(queryset, many=True)
    #     return Response(serializer.data)
