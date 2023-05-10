from django.urls import path
from .views import index, generate_qr

urlpatterns = [

    path('', index), # ola.com/barcode/
    path('url', generate_qr) # ola.com/barcode/url
 
]
