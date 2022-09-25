from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from problems.models.content import Content
from problems.serializers import ContentSerializer

class ContentsAPI(APIView):
    def get(self, request, pk = None, format = None):
        id = pk
        if id is not None:
            content = Content.objects.get(id = id)
            contentSerializer = ContentSerializer(content)
            return Response(contentSerializer.data, status= status.HTTP_200_OK)
        else:
            all_content = Content.objects.all()
            contentSerializer = ContentSerializer(all_content, many = True)
            return Response(contentSerializer.data, status= status.HTTP_200_OK)

    def post(self, request, format = None):
        contentSerializer = ContentSerializer(data = request.data)
        if contentSerializer.is_valid():
            contentSerializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(contentSerializer.errors, status = status.HTTP_400_BAD_REQUEST)
