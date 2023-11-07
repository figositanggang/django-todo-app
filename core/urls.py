from django.urls import path

from . import views

urlpatterns = [
    path("", views.TodoList.as_view(), name="todo_list"),
    path("todo/<int:pk>/", views.TodoView.as_view(), name="todo_detail"),
    path("new/", views.CreateTodo.as_view(), name="todo_new"),
    path("edit/<int:pk>/", views.UpdateTodo.as_view(), name="todo_edit"),
    path("delete/<int:pk>/", views.DeleteTodo.as_view(), name="todo_delete"),
]
