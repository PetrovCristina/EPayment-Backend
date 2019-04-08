
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()
router.register('images', UploadImageViewset, 'images')
urlpatterns = [
    path('current_user/', current_user),
    path('list/', list),
    path('users/', UserList.as_view()),
    path('', include(router.urls))

]