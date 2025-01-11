from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from users_tests.models import Test, Question, Answer #, UserAnswer


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class AnswerDetailSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ('name', 'image')


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'name', 'image', 'test')


class QuestionDetailSerializer(ModelSerializer):
    answers = SerializerMethodField

    def get_answers(self, obj):
        return AnswerSerializer(obj.ouestion.all, many=True).data

    class Meta:
        model = Question
        fields = ('name', 'answers')


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'name', 'body')


# class UserAnswerSerializer(ModelSerializer):
#     class Meta:
#         model = UserAnswer
#         fields = '__all__'
