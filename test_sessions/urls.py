from rest_framework.routers import SimpleRouter

from test_sessions.apps import TestSessionsConfig
from test_sessions.views import TestSessionViewSet, UserAnswerViewSet

app_name = TestSessionsConfig.name

router = SimpleRouter()
router.register(r'', TestSessionViewSet, basename='test_sessions')
router.register(r'user_answers', UserAnswerViewSet, basename='user_answers')


urlpatterns = []

urlpatterns += router.urls
