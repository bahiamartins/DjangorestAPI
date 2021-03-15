from django.urls import path
from authcustom.views import views as authcustom

urlpatterns = [
    path('', authcustom.login_view, name='login_view'),
]
