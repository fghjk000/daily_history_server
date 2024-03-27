from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from daily_history.models import Contents, Image


class ImageSerializer(ModelSerializer):
    id = serializers.FileField(required=True)

    class Meta:
        model = Image
        fields = ['id', 'image']


class ContentsSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = Contents
        fields = ['id', 'title', 'detail', 'created_at', 'images',]

    def create(self, validated_data):
        images_data = self.context.get('request').FILES.getlist('images')  # 이미지 업로드
        contents = Contents.objects.create(**validated_data)
        for image_data in images_data:
            Image.objects.create(contents=contents, image=image_data)
        return contents


