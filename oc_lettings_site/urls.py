from django.contrib import admin
from django.urls import path, include
from . import views
from . import settings
from django.conf.urls.static import static


def trigger_error(request):
    print('sentry-debug')
    division_by_zero = 1 / 0


urlpatterns = [
    path("", views.index, name="index"),
    path("", include("lettings.urls")),
    path("", include("profiles.urls")),
    path("admin/", admin.site.urls),
    path('sentry-debug/', trigger_error),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = views.handler404
handler500 = views.handler500
