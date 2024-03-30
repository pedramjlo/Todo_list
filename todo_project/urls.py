
from django.contrib import admin
from django.urls import path, include

from accounts import urls
from todo_list import urls


from rest_framework.authtoken import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path("", include("todo_list.urls")),
    path('api-token-auth/', views.obtain_auth_token),
]
