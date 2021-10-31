from apps.quiz_user.models import QuizUser

class InvalidPasswordException(Exception):
    pass

def create_user(username, email, password, confirm_password):
    if password != confirm_password:
        raise InvalidPasswordException
    return QuizUser.objects.create(
        username=username,
        email=email,
        password=password
    )