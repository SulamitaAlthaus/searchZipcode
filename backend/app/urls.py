from django.contrib import admin
from zipcode.views import ZipCodeViewSet
from rest_framework import routers
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'cep', ZipCodeViewSet)

urlpatterns = [
    path('homepage', include('app.urls')),
    path('admin/', admin.site.urls),
    path('cep', ZipCodeViewSet.as_view(
        {'get': 'list',
         'post': 'create'})),
    path('cep/<int:zipcode_id>', ZipCodeViewSet.as_view(
        {'delete': 'delete',
         'put': 'update'})),

]
