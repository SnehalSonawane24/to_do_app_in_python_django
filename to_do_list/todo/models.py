from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    priority = models.CharField(max_length=32)
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Task"
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


class TaskCategoryAssociation(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="tasks")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="categories"
    )

    class Meta:
        db_table = "Task Category Association"
        verbose_name = "Task Category Association"
        verbose_name_plural = "Task Category Associations"
        unique_together = ("task", "category")

    def __str__(self):
        return f"{self.task.title} - {self.category.name}"


class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    class Meta:
        db_table = "User"
        verbose_name = "User"
        verbose_name_plural = "Users"
        unique_together = ("user", "task")

    def __str__(self):
        return f"{self.user} - {self.task.name}"


class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Subtask"
        verbose_name = "Subtask"
        verbose_name_plural = "Subtasks"
        unique_together = ("task", "title")

    def __str__(self):
        return f"{self.task.name} - {self.title}"
