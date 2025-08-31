from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_view, name='register_view'),
    path('', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
    path('editProfile/', editProfile, name='editProfile'),
]