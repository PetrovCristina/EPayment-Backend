from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),

    #accounts
    path('', views.HomeView.as_view(), name='home'),
    #accounts/register
    path('register/', views.UserEntry.as_view(), name='user-entry'),
]