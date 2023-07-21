from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/store/', include('store.urls')),
    path('api/warehouse/', include('warehouse.urls')),
    path('admin/', admin.site.urls),
]
