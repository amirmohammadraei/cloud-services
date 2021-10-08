from django.contrib import admin
from django.urls import path
from core import views as core_views
from django.contrib.staticfiles.urls import static
from django.conf import settings


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', core_views.IndexView.as_view(template_name='index.html'), name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
