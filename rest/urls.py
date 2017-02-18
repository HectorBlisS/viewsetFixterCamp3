from django.conf.urls import url, include
from django.contrib import admin
from courses.api import urls as apiUrls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(apiUrls)),
]
