from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from todo.models import Task, Category, TaskCategoryAssociation, User, Subtask

@admin.register(Task)
class TaskAdmin(ImportExportModelAdmin):
    list_display = ['title', 'is_complete', 'priority', 'created_at', 'due_date']
    list_filter = ['due_date', 'created_at', 'is_complete']
    search_field = ['title']
    save_as = True


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['name', 'created_at']
    search_field = ['name']
    save_as = True


@admin.register(TaskCategoryAssociation)
class TaskCategoryAssociationAdmin(ImportExportModelAdmin):
    list_display = ['task', 'category']
    list_filter = ['task', 'category']
    search_field = ['task', 'category']
    save_as = True


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ['user', 'task']
    list_filter = ['user', 'task']
    search_field = ['user', 'task']
    save_as = True


@admin.register(Subtask)
class Subtask(ImportExportModelAdmin):
    list_display = ['task', 'title', 'is_completed', 'created_at']
    list_filter = ['task', 'title', 'created_at']
    search_field = ['task', 'title']
    save_as = True