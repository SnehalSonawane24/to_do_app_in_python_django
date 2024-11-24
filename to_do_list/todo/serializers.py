from todo.models import Task, Category, TaskCategoryAssociation, User, Subtask
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):

    class Meta():
        model = Task
        fields = ['title', 'description', 'is_complete', 'priority', 'due_date', 'created_at', 'update_at']


class CategorySerializer(serializers.ModelSerializer):

    class Meta():
        model = Category
        fields = ['name', 'created_at', 'updated_at']


class TaskCategoryAssociationSerializer(serializers.Serializer):

    class Meta():
        model = TaskCategoryAssociation
        fields = ['task', 'category']


class UserSerializer(serializers.Serializer):

    class Meta():
        model = User
        fields = ['user', 'task']


class SubtaskSerializer(serializers.Serializer):

    class Meta():
        model = Subtask
        fields = ['task', 'title', 'is_completed', 'created_at', 'updated_at']