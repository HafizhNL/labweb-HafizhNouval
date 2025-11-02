from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from basic_api import views

urlpatterns = [
    # API
    path('basic/', views.API_objects.as_view()),
    path('basic/<int:pk>/', views.API_detail_objects.as_view()),
    path('dosen/', views.API_dosen.as_view()),
    path('student/', views.API_student.as_view()),
    path('student/<int:pk>/', views.API_detail_student.as_view()),

    # CRUD
    path('basic_list/', views.post_list, name='post_list'),
    path('basic_create/', views.post_create, name='post_create'),
    path('basic_delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('basic_edit/<int:pk>/', views.post_edit, name='post_edit'),
]

urlpatterns = format_suffix_patterns(urlpatterns)