from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from users_tests.models import Test, Question, Answer


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
        fields = '__all__'


class QuestionDetailSerializer(ModelSerializer):
    answers = SerializerMethodField()

    def get_answers(self, obj):
        answers = Answer.objects.filter(question=obj)
        return [answer.name for answer in answers]

    class Meta:
        model = Question
        fields = ('id', 'name', 'answers',)


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class TestDetailSerializer(ModelSerializer):
    questions = SerializerMethodField()

    def get_questions(self, obj):
        questions = Question.objects.filter(test=obj)
        return [question.id for question in questions]

    class Meta:
        model = Test
        fields = ('id', 'name', 'questions',)
