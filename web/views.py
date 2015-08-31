from django.shortcuts import render

# Create your views here.
def BSIV(request):
	return render(request, 'BSIV.html')

def home(request):
	return render(request, 'home.html')

def us(request):
	return render(request, 'us.html')

def clients(request):
	return render(request, 'clients.html')

def downloads(request):
	return render(request, 'downloads.html')

def contact(request):
	return render(request, 'contact.html')