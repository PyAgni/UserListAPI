from rest_framework import serializers

from .models import User, Activity


class ActivitySerializerHelper(serializers.ModelSerializer):
	start_time = serializers.DateTimeField(format='%b %d %Y  %H:%M%p')
	end_time = serializers.DateTimeField(format="%b %d %Y  %H:%M%p")

	class Meta:
		model = Activity
		fields = ['start_time', 'end_time']


class UserSerializer(serializers.ModelSerializer):
	"""
	Nested Serializer for returning activities of different users
	"""
	activities = ActivitySerializerHelper(many=True, read_only=True)
	class Meta:
		model = User
		fields = ['user_id', 'real_name', 'tz', 'activities']

class ActivitySerializer(serializers.ModelSerializer):
	"""
	Serializer for Activity API end-points
	"""
	start_time = serializers.DateTimeField(format='%b %d %Y  %H:%M%p')
	end_time = serializers.DateTimeField(format="%b %d %Y  %H:%M%p")
	class Meta:
		model = Activity
		fields = ['user','start_time','end_time']