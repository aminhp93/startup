from rest_framework import serializers

from videos.models import Video


class VideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Video
		fields = [
			'id',
			'title',
			'url',
			'created_at',
			'updated_at'
		]
