from django.contrib import admin
from django.urls import path, include
import board.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board.views.home, name="home"),

    path('board/', include('board.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('accounts/', include('accounts.urls')),
    
    path('viewcrud/', include('viewcrud.urls')),
    path('classcrud/', include('classcrud.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
