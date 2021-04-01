
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('pwa.urls'))
]

# urlpatterns += i18n_patterns (
#     path('', include('blog.urls')),
# )
