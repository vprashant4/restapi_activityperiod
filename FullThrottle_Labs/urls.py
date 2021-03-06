from django.contrib import admin
from django.urls import path, include
from .router import routers

urlpatterns = [
    path('', include(routers.urls)),
    path('api/', include(routers.urls)),
    path('user/', include('fltapitest.urls')),
    path('admin/', admin.site.urls),

]
