from .views import *
from django.urls import path

urlpatterns = [
    path('password_generator/', PasswordGeneratorView.as_view(), name='password_generator'),
    path('file_converter/', FileConverterView.as_view(), name='file_converter'),
]