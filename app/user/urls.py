"""
URL mappings for the user API.
"""
from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
<<<<<<< HEAD
    path('create/', views.CreateUserView.as_view(), name='create'),
=======
    path('create/', Views.CreateUserView.as_view(), name='create'),
>>>>>>> 2a92dbb4a31e0055fa2ab6340d780f9b3d283e59
]
