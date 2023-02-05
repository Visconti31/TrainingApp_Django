from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('exercises/', views.getExercices),
    path('exercises/create/', views.createExercise),
    path('exercises/<str:pk>/', views.getExercice),
]