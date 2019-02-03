from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from accounts.models import User


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class HomeView(generic.ListView):
    #name of the object to be used in the index.html
    context_object_name = 'user_list'
    template_name = 'accounts/home_page.html'

    def get_queryset(self):
        return User.objects.all()

#view for the user entry page
class UserEntry(CreateView):
    model = User
    fields = ['user_name', 'user_avatar']