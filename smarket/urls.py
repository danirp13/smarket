
from django.conf.urls import  url, include
from django.contrib import admin

urlpatterns = [
	url(r'^tienda/', include('tienda.urls')),
    url(r'^admin/', admin.site.urls),
]
