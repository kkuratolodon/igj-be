from django.urls import path

from .views import RegisterView, UpdateUserView, UserDataView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('user-data/', UserDataView.as_view(), name='user-data'),
    path('update-user/', UpdateUserView.as_view(), name='update-user'),
]