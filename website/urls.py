from django.contrib import admin
from django.urls import path, include
# # from rest_framework import routers
# from django.conf.urls import urls
# from django.conf import settings
# from django.views.static import serve

urlpatterns = [
    # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', include('affiliate.urls')),
    
    # path('api-auth/', include('rest_framework.urls'))
]
