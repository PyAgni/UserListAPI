from rest_framework import viewsets

from .serializers import UserSerializer, ActivitySerializer
from .services import UserService
from .models import Activity


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = UserService.get_user_info()


class ActivityViewSet(viewsets.ModelViewSet):
	serializer_class = ActivitySerializer
	queryset = Activity.objects.all()