from django.urls import path
from .views import ProfileListView, ProfileView, logout_user, LoginView, RegisterUserView, UpdateUserView

urlpatterns = [
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profiles/', ProfileListView.as_view(), name='profile_list'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('update_user/', UpdateUserView.as_view(), name='update'),
]
