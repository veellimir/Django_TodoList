from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        telegram_id = self.request.query_params.get('telegram_id')
        if telegram_id:
            return Task.objects.filter(user__telegram_id=telegram_id)
        return Task.objects.all()

    def perform_create(self, serializer):
        telegram_id = self.request.data.get('user')

        from apps.users.models import Users
        user = Users.objects.get(telegram_id=telegram_id)
        serializer.save(user=user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
