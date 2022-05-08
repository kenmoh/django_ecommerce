
from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "STORE ADMIN"
admin.site.index_title = "STORE MANAGEMENT"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
]
