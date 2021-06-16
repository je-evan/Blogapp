from django.urls import path, reverse_lazy
from .views import SignupView, UserLoginView, UserLogoutView


urlpatterns = [
    path('signup/', SignupView.as_view(), name="signup"),
    path('login/', UserLoginView.as_view(template_name="user/login.html"), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
]
