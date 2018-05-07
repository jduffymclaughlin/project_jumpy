from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def other(request):
    return render(request, 'basic_app/other.html')

def about_us(request):
    return render(request, 'basic_app/about_us.html')

def what_we_do(request):
    return render(request, 'basic_app/what_we_do.html')

def service_pricing(request):
    return render(request, 'basic_app/service_pricing.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')

def contact(request):
    return render(request, 'basic_app/contact.html')
