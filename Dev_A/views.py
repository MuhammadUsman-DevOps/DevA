from django.shortcuts import render


def index(request):
    return render(request, template_name="wsite/index.html")


def about_us(request):
    return render(request, template_name="wsite/about-us.html")


def services(request):
    return render(request, template_name="wsite/services.html")


def portfolio(request):
    return render(request, template_name="wsite/portfolio.html")


def contact_us(request):
    return render(request, template_name="wsite/contact.html")
