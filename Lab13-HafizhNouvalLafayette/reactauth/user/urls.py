from django.urls import path, include
from .views import RegisterView, CustomTokenObtainPairView, EvaluationView, EvaluationDetail, UserListView
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('evaluation/', EvaluationView.as_view(), name='evaluation'),
    path('evaluation/<int:pk>/', EvaluationDetail.as_view(), name='evaluation_detail'),
    path('users/', UserListView.as_view(), name='user_list'),
]
