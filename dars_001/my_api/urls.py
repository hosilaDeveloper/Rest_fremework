from django.urls import path
from .views import (TodoList, TodoCreate, TodoDetail,
                    TodoUpdate,
                    TodoDelete,
                    TodoListCreate,
                    TodoRUD)


urlpatterns = [
    path('', TodoList.as_view(), name='todo-list'),
    path('create/', TodoCreate.as_view(), name='todo-create'),
    path('<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
    path('<int:pk>/update/', TodoUpdate.as_view(), name='todo-update'),
    path('<int:pk>/delete/', TodoDelete.as_view(), name='todo-delete'),
    path('todo-list/', TodoListCreate.as_view(), name='todo-list-create'),
    path('todo-list/<int:pk>/', TodoRUD.as_view(), name='todo-rud')
]