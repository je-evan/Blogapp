from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from postapp import settings
from django.shortcuts import resolve_url
from .forms import SignupForm

class SignupView(CreateView):
    form_class = SignupForm
    template_name = "user/signup.html"
    success_url = reverse_lazy("login")


class UserLoginView(LoginView):
    
    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS,
            'You are successfully logged in!'
        )
        return resolve_url(settings.LOGIN_REDIRECT_URL)
        


class UserLogoutView(LogoutView):
    
    def get_next_page(self):
        next_page = reverse_lazy('post') 
        messages.add_message(
            self.request, messages.SUCCESS,
            'You are successfully logged out!'
        )
        return next_page