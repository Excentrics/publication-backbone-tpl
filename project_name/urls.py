from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from filebrowser.sites import site
from django.contrib.sites.models import Site
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^robots.txt$',
       TemplateView.as_view(template_name='robots.txt',
                            content_type='text/plain',
                            get_context_data=lambda: {'domain': Site.objects.get_current().domain},),
       name='robots.txt'),
    url(r'^', include('publication_backbone.sitemap.urls'), name='sitemap'),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/salmonella/', include('salmonella.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('publication_backbone.urls')),
    url(r'', include('fluent_pages.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns