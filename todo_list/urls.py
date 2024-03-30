from django.urls import path

from .views import CreateTask, CreateCategory, GetTasks, GetCategories, DeleteTask, DeleteCategory, UpdateCategory, UpdateTask, GetTask, GetCategory

urlpatterns = [
    path('create_task/', CreateTask.as_view(), name='create_task'),
    path('create_category/', CreateCategory.as_view(), name='create_category'),

    path('get_tasks/', GetTasks.as_view(), name='get_tasks'),
    path('get_task/<int:pk>', GetTask.as_view(), name='get_task'),

    path('get_categories/', GetCategories.as_view(), name='get_categories'),
    path('get_category/<int:pk>', GetCategory.as_view(), name='get_category'),

    path('update_task/<int:pk>', UpdateTask.as_view(), name='update_task'),
    path('update_category/<int:pk>', UpdateCategory.as_view(), name='update_category'),

    path('delete_task/<int:pk>', DeleteTask.as_view(), name='delete_task'),
    path('delete_category/<int:pk>', DeleteCategory.as_view(), name='delete_category'),


]
