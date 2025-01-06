from rest_framework.routers import SimpleRouter

from users_tests.apps import UsersTestsConfig
from users_tests.views import TestViewSet, QuestionViewSet, AnswerViewSet, UserAnswerViewSet

app_name = UsersTestsConfig.name

router = SimpleRouter()
router.register(r'tests', TestViewSet, basename='tests')
router.register(r'questions', QuestionViewSet, basename='questions')
router.register(r'answers', AnswerViewSet, basename='answers')
router.register(r'user_answers', UserAnswerViewSet, basename='user_answers')

urlpatterns = []

urlpatterns += router.urls
