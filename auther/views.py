from django.shortcuts import render
from .models import ContactUs


# Create your views here.
def contactus(request):
    if request.method=='POST':
        Email = request.POST.get('email')
        Message = request.POST.get('message')
        data = ContactUs(email=Email, message=Message)
        data.save()

    return render(request, 'contactus.html')


def aboutus(request):
    return render(request, 'aboutus.html')
