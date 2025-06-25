from rest_framework import serializers

from apps.users.models import Users
from .models import Task, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name", read_only=True)
    username = serializers.CharField(write_only=True)
    category_name = serializers.CharField(write_only=True)

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'due_date',
            'created_at',
            'category',
            'user',
            'username',
            'category_name'
        ]
        read_only_fields = ['id', 'created_at', 'user', 'category']

    def create(self, validated_data):
        username = validated_data.pop("username")
        category_name = validated_data.pop("category_name")

        validated_data.pop("user", None)
        validated_data.pop("category", None)

        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            raise serializers.ValidationError(
                {"telegram_id": "Пользователь не найден"}
            )

        try:
            category = Category.objects.get(name__iexact=category_name)
        except Category.DoesNotExist:
            raise serializers.ValidationError(
                {"category_name": "Категория не найдена"}
            )
        return Task.objects.create(user=user, category=category, **validated_data)

