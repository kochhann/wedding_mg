from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
]

admin.site.site_header = 'Gestão Vão se casar'
admin.site.site_title = 'Gestão Vão se casar'
admin.site.index_title = 'Área Administrativa'