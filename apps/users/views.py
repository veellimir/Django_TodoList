from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Users
from .serializers import UserSerializer


@api_view(['GET'])
def get_user_by_name(request, username: str):
    try:
        user = Users.objects.get(username=username)
    except Users.DoesNotExist:
        return Response(
            {"detail": "Пользователь не найден"},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = UserSerializer(user)
    return Response(serializer.data)
