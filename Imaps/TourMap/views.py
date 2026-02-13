from django.shortcuts import render

# Create your views here.
def WelcomeHomeOdisha(request):
    return render(request, 'WelcomeHomeOdisha.html')             
def UshaKothiWildlifeSanctuary(request):
    return render(request, 'UshaKothiWildlifeSanctuary.html')   
def SimilipalNationalPark(request):
    return render(request, 'SimilipalNationalPark.html')
def KonarkSunTemple(request):
    return render(request, 'KonarkSunTemple.html')      
def JagannathPuri(request):
    return render(request,'JagannathPuri.html')
def ChilikaLake(request):
    return render(request,'ChilikaLake.html')   

