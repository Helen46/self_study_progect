from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from  rest_framework.viewsets import ModelViewSet

from test_sessions.models import TestSession, UserAnswer
from test_sessions.serializers import TestSessionSerializer, UserAnswerSerializer
from users.permissions import IsAdmin, IsYourObject


class TestSessionViewSet(ModelViewSet):
    queryset = TestSession.objects.all()
    serializer_class = TestSessionSerializer

    def perform_create(self, serializer):
        test_session = serializer.save()
        test_session.user = self.request.user
        test_session.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (IsAuthenticated,)
        elif self.action == 'retrieve':
            self.permission_classes = (IsAdmin | IsYourObject)
        else:
            self.permission_classes = (IsAdmin,)

        return super().get_permissions()

class UserAnswerViewSet(ModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer

    def post(self, request):
        return Response({'message': 'POST request successful'})

    def perform_create(self, serializer):
        user_answer = serializer.save
        user_answer.user = self.request.user
        user_answer.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (IsAuthenticated,)
        elif self.action == 'destroy':
            self.permission_classes = (IsAdmin,)
        else:
            self.permission_classes = (IsAdmin | IsYourObject)

        return super().get_permissions()
