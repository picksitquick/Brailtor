from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'solve'

urlpatterns = [
    re_path(r'^indexx.html/$',views.indexx,name='indexx'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + staticfiles_urlpatterns()
