from django.db.models import QuerySet
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from daily_history.models import Contents, Image
from daily_history.serializer import ContentsSerializer, ImageSerializer


class ContentsListCreateAPI(APIView):
    def get(self, request):
        contents = Contents.objects.prefetch_related('images').all()
        return_data = ContentsSerializer(contents, many=True).data
        return Response(return_data, status=200)

    def post(self, request):
        serializer = ContentsSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        contents: Contents = Contents.objects.create(
            title=serializer.validated_data['title'],
            detail=serializer.validated_data['detail'],
        )
        return_data = ContentsSerializer(contents).data
        return Response(return_data, status=201)


class ContentsDetailAPI(APIView):
    def get(self, request, contents_id):
        contents = get_object_or_404(Contents, id=contents_id)
        contents_data = ContentsSerializer(contents).data
        return Response(contents_data, status=200)

    def put(self, request, contents_id):
        contents = get_object_or_404(queryset=Contents, id=contents_id)
        serializer = ContentsSerializer(instance=contents, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=200)

    def patch(self, request, contents_id):
        contents = get_object_or_404(queryset=Contents, id=contents_id)
        serializer = ContentsSerializer(instance=contents, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=200)

    def delete(self, request, contents_id):
        get_object_or_404(Contents, id=contents_id).delete()
        return Response(status=204)


class ImageListCreateAPI(APIView):
    def post(self, request, contents_id):
        serializer = ImageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image: Image = Image.objects.create(
            contents_id=contents_id,  # 내용과 이미지를 연결
            image=serializer.validated_data['image'],
        )
        return_data = ImageSerializer(image).data
        return Response(return_data, status=201)


class ImageDetailAPI(APIView):
    def delete(self, request, image_id):
        get_object_or_404(Image, id=image_id).delete()
        return Response(status=204)
