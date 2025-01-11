from rest_framework.serializers import ModelSerializer

from test_sessions.models import TestSession, UserAnswer
from users_tests.serializers import TestSerializer, QuestionDetailSerializer


class TestSessionSerializer(ModelSerializer):
    test = TestSerializer

    class Meta:
        model = TestSession
        fields = ('test',)


class UserAnswerSerializer(ModelSerializer):
    question = QuestionDetailSerializer

    class Meta:
        model = UserAnswer
        fields = ('question', 'body',)