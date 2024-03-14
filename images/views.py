from requests import Request
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.parsers import MultiPartParser, FormParser

from images.serializers import ImageSerializer


class ImageUploadView(APIView):
    # parser_classes = MultiPartParser
    serializer_class = ImageSerializer

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request: Request, *args, **kwargs):
        # request.data["user"] = request.user.pk
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
