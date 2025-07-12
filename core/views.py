# core/views.py

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View

class LogoutGetView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')
