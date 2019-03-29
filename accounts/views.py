from accounts.models import User
from django.contrib.auth.models import User
from rest_framework import permissions, status, generics, parsers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken, ProfilePictureSerializer


# view for the image upload
class ProfilePictureView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProfilePictureSerializer
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser,)

    def perform_create(self, serializer):
        print(self.request.FILES['profile_pic'])
        serializer.save(user=User.objects.get(pk=2))


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    @staticmethod
    def post(request):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
