from django.contrib import admin

from Dev_A.models import HeroSection, CompanyInfo, Testimonial, SocialMedia, CompanyLocation

admin.site.site_header = "DevA+ Administration Panel"
admin.site.index_title = "DevA+ Administration"

admin.site.register(HeroSection)
admin.site.register(CompanyInfo)
admin.site.register(Testimonial)
admin.site.register(SocialMedia)
admin.site.register(CompanyLocation)