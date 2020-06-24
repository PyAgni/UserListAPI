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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'ok':True,
            'members':serializer.data,
            }
        	)

class ActivityViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing activity instances.
    """
	serializer_class = ActivitySerializer
	queryset = Activity.objects.all()
