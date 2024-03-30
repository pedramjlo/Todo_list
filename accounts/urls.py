from django.urls import path

from .views import RegisterView, LoginView, ListUser

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('all_users/', ListUser.as_view(), name='all_users')
]
