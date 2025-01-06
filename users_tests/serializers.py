from rest_framework.serializers import ModelSerializer

from users_tests.models import Test, Question, Answer, UserAnswer


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class UserAnswerSerializer(ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = '__all__'