from rest_framework import serializers

from .models import User, Activity


class ActivitySerializerHelper(serializers.ModelSerializer):
	class Meta:
		model = Activity
		fields = ['start_time', 'end_time']


class UserSerializer(serializers.ModelSerializer):
	activities = ActivitySerializerHelper(many=True, read_only=True)
	class Meta:
		model = User
		fields = ['user_id', 'real_name', 'tz', 'activities']

class ActivitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Activity
		fields = ['user','start_time','end_time']