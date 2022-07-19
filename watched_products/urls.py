from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'watched_products'

urlpatterns = [

    path('watch_list/update-watch_list', views.update_watch_list, name="update-watch_list"),

]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
