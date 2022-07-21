from re import A
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from agora.views import Agora

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('connection.urls')),
    path('agora/', Agora.as_view(
        app_id='a92dcfe3b54442f29716549a58080bf9',
        channel='123',
    ))


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 