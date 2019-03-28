from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from accounts.serializers import AccountsSerializer, ProfilePictureSerializer
from accounts.models import User
from rest_framework.generics import CreateAPIView
from rest_framework import parsers, permissions, generics

class HomeView(CreateAPIView):
   # name of the object to be used in the index.html
    context_object_name = 'user_list'
    template_name = 'accounts/home_page.html'
    serializer_class = AccountsSerializer

    def get_queryset(self):
        return User.objects.all()

#view for the user entry page
class UserEntry(CreateView):
    model = User
    fields = ['user_name', 'user_surname', 'user_phone', 'user_email', 'user_pass']

#view for the image upload
class ProfilePictureView(generics.CreateAPIView):

    permission_classes = (permissions.AllowAny,)
    serializer_class = ProfilePictureSerializer
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser,)

    def perform_create(self, serializer):

        print(self.request.FILES['profile_pic'])
        serializer.save(user=User.objects.get(pk=2))