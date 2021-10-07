from django.contrib import admin
from django.urls import path
from core import views as core_views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', core_views.IndexView.as_view(template_name='index.html'), name='index'),
]
