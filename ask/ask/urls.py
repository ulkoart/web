from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from qa.views import test, main, popular, question_detail, aks


urlpatterns = [
    url(r'^$', main),
    url(r'^login/$', test),
    url(r'^signup/$', test),
    url(r'^question/(?P<pk>[0-9]+)/$', question_detail, name='question_detail'),
    url(r'^ask/$', aks),
    url(r'^popular/$', popular),
    url(r'^new/$', test),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    pass
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
