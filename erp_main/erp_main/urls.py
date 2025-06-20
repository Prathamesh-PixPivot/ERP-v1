from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('user_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/crm/', include('crm.urls')),
    path('api/finance/', include('finance.urls')),
    path('api/hrms/', include('hrms.urls')),
    path('api/inventory/', include('inventory.urls')),
    path('api/itam/', include('itam.urls')),
    path('api/itsm/', include('itsm.urls')),
    path('api/itom/', include('itom.urls')),
    path('api/vms/', include('vms.urls')),
    path('api/gst/', include('gst.urls')),
]

