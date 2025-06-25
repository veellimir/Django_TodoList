from rest_framework import viewsets

from apps.users.models import Users
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        telegram_id = self.request.query_params.get('telegram_id')
        try:
            if telegram_id:
                user = Users.objects.get(telegram_id=int(telegram_id))
                tasks = Task.objects.filter(user=user)
                return tasks
            tasks = Task.objects.all()
            return tasks
        except Users.DoesNotExist:
            return Task.objects.none()
        except Exception as e:
            raise

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__iexact=name)
        return queryset
