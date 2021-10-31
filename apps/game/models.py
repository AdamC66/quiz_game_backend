from django.db import models
from quiz.utils.helpers import code_generator
from apps.quiz_user.models import QuizUser

def game_code_generator():
    return code_generator("GME", 20)
class GameBoard(models.Model):
    user=models.ForeignKey(QuizUser, related_name="game_boards", on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=30, unique=True, default=game_code_generator)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    name = models.CharField(max_length=255)


def category_code_generator():
    return code_generator("CTG", 20)
class Category(models.Model):
    code = models.CharField(max_length=30, unique=True, default=category_code_generator)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    game_board = models.ForeignKey(GameBoard, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=255)
    

def question_code_generator():
    return code_generator("QUE", 20)
class Question(models.Model):
    code = models.CharField(max_length=30, unique=True, default=question_code_generator)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="questions")
    points = models.IntegerField(default=0)
    answer = models.TextField()
    question = models.CharField(max_length=255)

    