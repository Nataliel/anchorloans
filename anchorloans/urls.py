from django.conf.urls import patterns, include, url
from django.contrib import admin
from anchorloans import settings
from core.views import HomeTemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^resullt/$', 'core.views.coinDeterminer', name='result'),
)
