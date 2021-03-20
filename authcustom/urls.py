from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import login_view

urlpatterns = [
    path('', login_view, name='login_view'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
