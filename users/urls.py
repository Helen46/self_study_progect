from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListApiView, UserRetrieveApiView, UserUpdateApiView, UserDestroyApiView

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path("list/", UserListApiView.as_view(), name="list"),
    path("user/<int:pk>/", UserRetrieveApiView.as_view(), name="user_retrieve"),
    path("user/update/<int:pk>/", UserUpdateApiView.as_view(), name="user_update"),
    path("user/delete/<int:pk>/", UserDestroyApiView.as_view(), name="user_delete"),
]
