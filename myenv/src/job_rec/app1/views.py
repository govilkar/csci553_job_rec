from django.shortcuts import render

# Create your views here.

def landing_page(request, *args, **kwargs) :
	context = {}
	return render(request, 'landing_page.html', context)

