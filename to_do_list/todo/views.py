from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from todo.models import Task, Category, TaskCategoryAssociation, User, Subtask
from todo.serializers import TaskSerializer, CategorySerializer, TaskCategoryAssociationSerializer, UserSerializer, SubtaskSerializer
# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [
        DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ("title", "is_complete")
    search_fields = ("title")
    ordering_fields = ("is_complete", "created_at", "updated_at")