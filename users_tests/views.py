# from drf_yasg.openapi import Response
# from rest_framework import status
# from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from users.permissions import IsAdmin, IsTeacher, IsAutor
from users_tests.models import Test, Question, Answer
from users_tests.serializers import TestSerializer, QuestionSerializer, AnswerSerializer, \
    QuestionDetailSerializer, AnswerDetailSerializer, TestDetailSerializer


# class TestSessionAPIView(APIView):
#   queryset = Question
#   permission_classes = (IsAuthenticated,)
#
#     def post(self, request, pk):

    #
    #     body = Question.objects.filter(test__id=pk)
    #     answers = UserAnswer(question=question, body=body)
    #     user_answer.save()
    #     return Response(status=status.HTTP_200_OK) #fron django.http import JsonResponse

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
