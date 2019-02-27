from django.conf.urls import url
from django.contrib import admin
from Blog   import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$/',views.index),
    url(r'^about/',views.about),
    url(r'^contact/',views.contact),
    url(r'^blog/',views.blog),
]

