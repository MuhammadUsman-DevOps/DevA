from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from Dev_A.models import HeroSection, CompanyInfo, Testimonial, CompanyLocation

hero_section = HeroSection.objects.first()
company_info = CompanyInfo.objects.first()
company_location = CompanyLocation.objects.first()
testimonial = Testimonial.objects.all()


def index(request):
    hero_section = ""
    company_info = ""
    testimonial = ""
    company_location = ""
    try:
        hero_section = HeroSection.objects.first()
        company_info = CompanyInfo.objects.first()
        company_location = CompanyLocation.objects.first()
        testimonial = Testimonial.objects.all()
        # TODO catch exception like ==> except Exception as e:
    except:
        print("something went wrong")

    context = {
        'hero_section': hero_section,
        'company_info': company_info,
        'testimonial': testimonial,
        'company_location': company_location
    }
    return render(request, template_name="wsite/index.html", context=context)


def about_us(request):
    context = {
        'hero_section': hero_section,
        'company_info': company_info,
        'testimonial': testimonial,
        'company_location': company_location
    }
    return render(request, template_name="wsite/about-us.html", context=context)


def services(request):
    context = {
        'hero_section': hero_section,
        'company_info': company_info,
        'testimonial': testimonial,
        'company_location': company_location
    }
    return render(request, template_name="wsite/services.html", context=context)


def portfolio(request):
    context = {
        'hero_section': hero_section,
        'company_info': company_info,
        'testimonial': testimonial,
        'company_location': company_location
    }
    return render(request, template_name="wsite/portfolio.html", context=context)


def contact_us(request):
    if request.method == "POST":
        sent = send_mail(
            request.POST.get("subject"),
            'first_name: ' + request.POST.get("firstname") + '\n'
            'last_name: ' + request.POST.get("lastname") + '\n'
            'phone: ' + request.POST.get("phone") + '\n'
            'email: ' + request.POST.get("email") + '\n'
            'Message: ' + request.POST.get("message") + '.',
            'from@example.com',
            ['osmanamin689@gmail.com'],
            fail_silently=False,
        )
        print("sent", sent)
        if sent:
            messages.success(request, "Your message has been sent. Thank you!")
            return HttpResponse("OK")

    context = {
        'hero_section': hero_section,
        'company_info': company_info,
        'testimonial': testimonial,
        'company_location': company_location
    }
    return render(request, template_name="wsite/contact.html", context=context)
