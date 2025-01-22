from django.urls import path
from rest_framework.routers import SimpleRouter

from courses.apps import CoursesConfig
from courses.views import CourseViewSet, LessonListApiView, LessonCreateApiView, LessonRetrieveApiView, \
    LessonUpdateApiView, LessonDestroyApiView

app_name = CoursesConfig.name

router = SimpleRouter()
router.register(r'', CourseViewSet, basename='courses')

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lessons_list"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lessons_create"),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="lessons_retrieve"),
    path("lessons/update/<int:pk>/", LessonUpdateApiView.as_view(), name="lessons_update"),
    path("lessons/delete/<int:pk>/", LessonDestroyApiView.as_view(), name="lessons_delete"),
]

urlpatterns += router.urls
