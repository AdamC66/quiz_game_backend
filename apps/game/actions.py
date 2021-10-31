from apps.game.models import GameBoard, Category, Question

def create_game(user, name):
    return GameBoard.objects.create(user=user, name=name)


def create_category(game_board, name):
    return Category.objects.create(game_board=game_board, name=name)


def create_question(category, name):
    return Question.objects.create(category=category, name=name)