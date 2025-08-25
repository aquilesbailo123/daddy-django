from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django_otp.admin import OTPAdminSite

from users.urls import urlpatterns as users_urlpatterns

admin.site.__class__ = OTPAdminSite
# admin.autodiscover()
# admin.site.enable_nav_sidebar = False

# No longer needed
# class NullView(View):
#     pass

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns.extend(users_urlpatterns)