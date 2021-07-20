from django.shortcuts import render
from . models import Details
# Create your views here.
def index(request):
    return render(request,'loginapp/one.html')
def success(request):
    request.POST.get('')
    firstname=request.POST.get('firstname')
    lastname=request.POST.get('lastname')
    username=request.POST.get('username')
    email=request.POST.get('email')
    password=request.POST.get('password')
    state=request.POST.get('sender')
    city=request.POST.get('city')
    address=request.POST.get('address')
    pincode=request.POST.get('pincode')
    if(Details.objects.filter(firstname=firstname,lastname=lastname,email=email,password=password)):
        return render(request,'loginapp/one.html')
    else:
        Details.objects.create(firstname=firstname,lastname=lastname,email=email,username=username,password=password,state=state,city=city,address=address,pincode=pincode)
            
        return render(request,'loginapp/success.html')
def view(request):
    doctor=Details.objects.filter(typeofperson='Doctor')
    patient=Details.objects.filter(typeofperson='Patient')
    return render(request,'loginapp/Doctorpatient.html',{'doctor':doctor,'patient':patient})