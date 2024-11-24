from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views import TodoViewSet


router = DefaultRouter()
router.register("api/todo", TodoViewSet, basename="todo")
urlpatterns = router.urls