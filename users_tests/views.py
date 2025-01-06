from rest_framework.viewsets import ModelViewSet

from users_tests.models import Test, Question, Answer, UserAnswer
from users_tests.serializers import TestSerializer, QuestionSerializer, AnswerSerializer, UserAnswerSerializer


class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class UserAnswerViewSet(ModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
