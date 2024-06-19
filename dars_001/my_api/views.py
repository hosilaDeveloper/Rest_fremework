from .models import Todo
from .serializer import TodoSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.


class TodoList(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoCreate(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoUpdate(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDelete(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoListCreate(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoRUD(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


