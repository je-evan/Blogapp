from .views import *
from django.urls import path

urlpatterns = [
    path('password_generator/', PasswordGeneratorView.as_view(), name='password_generator'),
    path('file_converter/', FileConverterView.as_view(), name='file_converter'),
    path('send_email/', subscribe, name='send_email'),
    path('analyze_sentiment/', analyze_sentiment, name='analyze_sentiment'),
]