from django.urls import path
from .views import *

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name='logout'),
    path('photos/', PhotoList.as_view(), name='photo-list'),
    path('photos/<int:pk>/', PhotoDetail.as_view(), name='photo-detail'),
]
