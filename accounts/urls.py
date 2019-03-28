from django.urls import path
from accounts import views
from accounts.views import UserEntry
from accounts.views import HomeView
from accounts.views import ProfilePictureView

app_name = 'accounts'

urlpatterns = [
    path('create/', HomeView.as_view()),
    #accounts
    path('', views.HomeView.as_view(), name='home'),
    #accounts/register
    path('register/', views.UserEntry.as_view(), name='user-entry'),
    #accounts/profile-pic
    path('profile-pic/', views.ProfilePictureView.as_view(), name='user-entry'),
]