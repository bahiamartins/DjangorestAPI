from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from authcustom.api import viewsets as v

router = routers.DefaultRouter()
router.register(r'users', v.UserViewSet, basename='users')

urlpatterns = [
    path('', include('authcustom.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
