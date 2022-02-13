from django.db import models


class HeroSection(models.Model):
    pic1 = models.ImageField(upload_to="images/", null=True, blank=True)
    pic2 = models.ImageField(upload_to="images/", null=True, blank=True)

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"


class CompanyInfo(models.Model):
    value = models.TextField(null=True, blank=True)
    chooseUs = models.TextField(null=True, blank=True)
    weOffer = models.TextField(null=True, blank=True)
    servicesOverview = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to="images/", null=True, blank=True)
    favicon = models.ImageField(upload_to="images/", null=True, blank=True)

    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural = "Company Information"

    def __str__(self):
        return self.value


class Testimonial(models.Model):
    client_name = models.CharField(max_length=50, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    clint_pic = models.ImageField(upload_to="images/", null=True, blank=True)
    client_text = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonial"

    def __str__(self):
        return self.client_name


class SocialMedia(models.Model):
    facebook = models.URLField(null=True, blank=True)
    Insta = models.URLField(null=True, blank=True)
    Linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Media"

    def __str__(self):
        return self.facebook


class CompanyLocation(models.Model):
    number = models.CharField(max_length=20, null=True, blank=True)
    mail = models.EmailField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
