from apps.game.models import GameBoard, Category, Question
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            "code",
            "question",
            "answer",
            "points"
        ]

class CategorySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = Category
        fields = [
            "name",
            "code",
            "questions",
        ]


class GameBoardSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    class Meta:
        model = GameBoard
        fields = [
            "name",
            "code",
            "categories",
        ]


class GameBoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameBoard
        fields = [
            "name",
            "code",
        ]
