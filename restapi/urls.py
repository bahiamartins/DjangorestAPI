from django.contrib import admin
from django.urls import path, include

# REST
from authcustom.views import api_views as api_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authcustom.urls')),
    path('api/', include('rest_framework.urls')),
    path('api/users/create/', api_views.UserCreate.as_view(), name='user_create'),
    path('api/users/', api_views.UserList.as_view(), name='user_list'),
    path('api/users/auth/', api_views.UserListAuth.as_view(), name='user_list_auth'),
    path('api/users/<int:pk>/', api_views.user, name='user_detail'),
]
