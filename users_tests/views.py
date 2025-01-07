from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.permissions import IsAdmin, IsTeacher, IsAutor, IsYourObject
from users_tests.models import Test, Question, Answer, UserAnswer
from users_tests.serializers import TestSerializer, QuestionSerializer, AnswerSerializer, UserAnswerSerializer


class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def perform_create(self, serializer):
        test = serializer.save()
        test.autor = self.request.user
        test.save()

    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = (IsAuthenticated,)
        elif self.action == 'create':
            self.permission_classes = (IsAdmin | IsTeacher,)
        else:
            self.permission_classes = (IsAdmin | IsAutor,)

        return super().get_permissions()


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        question = serializer.save()
        question.autor = self.request.user
        question.save()

    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = (IsAuthenticated,)
        elif self.action == 'create':
            self.permission_classes = (IsAdmin | IsTeacher,)
        else:
            self.permission_classes = (IsAdmin | IsAutor,)

        return super().get_permissions()


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        answer = serializer.save()
        answer.autor = self.request.user
        answer.save()

    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = (IsAuthenticated,)
        elif self.action == 'create':
            self.permission_classes = (IsAdmin | IsTeacher,)
        else:
            self.permission_classes = (IsAdmin | IsAutor,)

        return super().get_permissions()


class UserAnswerViewSet(ModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer

    def perform_create(self, serializer):
        user_answer = serializer.save()
        user_answer.user = self.request.user
        user_answer.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (IsAuthenticated,)
        elif self.action in('retrieve', 'list'):
            self.permission_classes = (IsAdmin | IsYourObject,)
        else:
            self.permission_classes = (IsAdmin,)

        return super().get_permissions()
