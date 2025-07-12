from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import LogoutGetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('login/',  auth_views.LoginView.as_view(), name='login'),
    path('logout/', LogoutGetView.as_view(), name='logout'),
]
