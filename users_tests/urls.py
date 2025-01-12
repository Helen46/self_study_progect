from django.urls import path
from rest_framework.routers import SimpleRouter

from users_tests.apps import UsersTestsConfig
from users_tests.views import TestViewSet, QuestionViewSet, AnswerViewSet, \
TestSessionAPIView

app_name = UsersTestsConfig.name

router = SimpleRouter()
router.register(r'tests', TestViewSet, basename='tests')
router.register(r'questions', QuestionViewSet, basename='questions')
router.register(r'answers', AnswerViewSet, basename='answers')

urlpatterns = [
    path('test_session/', TestSessionAPIView.as_view(), name='test_session')
]

urlpatterns += router.urls
