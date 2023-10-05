from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from . import settings
from django.conf.urls.static import static
from django.views.static import serve


def trigger_error(request):
    1 / 0


urlpatterns = [
    path("", views.index, name="index"),
    path("", include("lettings.urls")),
    path("", include("profiles.urls")),
    path("admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = views.handler404
handler500 = views.handler500
