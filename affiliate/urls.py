from django.urls import path, include
from . import views
# from django.urls import path, include
# # from rest_framework import routers
# # from django.conf.urls import urls
# from django.conf import settings
# from django.views.static import serve

# router = routers.DefaultRouter()
# router.register('services', views.ServiceView)
# from django.conf.urls import url

urlpatterns = [
	# url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
	# url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
	path('', views.home, name="home"),
	path('home.html', views.home, name="home"),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('contact.html', views.contact, name="contact"),
]

# from django.urls import path, include
# from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets

# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]