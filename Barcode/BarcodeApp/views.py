from django.http import HttpResponse
from django.shortcuts import render
import qrcode

# Create your views here.



def index(request):
    return render(request, 'forms.html')



def generate_qr(request):
    # get a url from user 
    user_url =  request.POST.get('url')

    qr_img = qrcode.make(user_url)

    qr_img.save("./BarcodeApp/static/BarcodeApp/images/image-qr-code.png")

    return render(request, 'index.html')
    