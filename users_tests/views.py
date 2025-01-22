from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from users.permissions import IsAdmin, IsTeacher, IsAutor
from users_tests.models import Test, Question, Answer
from users_tests.serializers import TestSerializer, QuestionSerializer, AnswerSerializer, \
    QuestionDetailSerializer, AnswerDetailSerializer, TestDetailSerializer


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

    def get_serializer_class(self):
        if self.action == 'retrieve':
            self.serializer_class = TestDetailSerializer

        return super().get_serializer_class()


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

    def get_serializer_class(self):
        if self.action == 'retrieve':
            self.serializer_class = QuestionDetailSerializer

        return super().get_serializer_class()


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

    def get_serializer_class(self):
        if self.action == 'retrieve':
            self.serializer_class = AnswerDetailSerializer

        return super().get_serializer_class()


class TestSessionAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        question_id = self.request.data.get('question')
        question = get_object_or_404(Question, id=question_id)
        correct_answer = Answer.objects.filter(question=question, is_correct=True).first().name
        user_answer = self.request.data.get('user_answer')


        if user_answer == correct_answer:
            message = 'Ответ верный'
        else:
            message = 'Ответ не верный'
        return Response({'message': message})
