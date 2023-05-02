from django.urls import path
from .views import index, generate_qr

urlpatterns = [

    path('', index),
    path('url', generate_qr)
]
