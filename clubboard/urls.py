from django.urls import path
from . import views

urlpatterns = [
    path('', views.club_list, name='club_list'),
    path('', views.post_list, name='post_list'),
    path('club/<int:pk>/', views.club_detail, name='club_detail'),
    path('club/new/', views.post_new, name='post_new'),
]