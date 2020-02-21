from rest_framework import viewsets, permissions

from .serializers import TodoSerializer
from todos.models import Todo


class TodoViewSet(viewsets.ModelViewSet):
    # queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Todo.objects.all()
        else:
            return self.request.user.todos.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
