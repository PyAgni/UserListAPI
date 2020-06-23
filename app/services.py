from rest_framework.response import Response

from .models import User, Activity
from .serializers import UserSerializer


class UserService(object):
	"""
	"""
	@staticmethod
	def get_user_info():
		user_data = User.objects.all()
		return user_data
