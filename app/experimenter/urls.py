from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^api/v1/experiments/', include('experimenter.experiments.urls')),
    url(r'^new/projects/', include('experimenter.projects.urls')),
    url(r'^', admin.site.urls),
]

if settings.DEBUG:  # pragma: no cover
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
