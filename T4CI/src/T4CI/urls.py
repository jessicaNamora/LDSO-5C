from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView


urlpatterns = [
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^overview/$', 'app.views.overview', name='overview'),
    url(r'^contact/$', 'app.views.contact', name='contact'),
    url(r'^about/$', 'app.views.about', name='about'),
    url(r'^profile/$', 'app.views.profile', name='profile'),
    url(r'^mydreams/$','T4CI.views.dreams', name='mydreams'),
    url(r'mydreams/$', RedirectView.as_view(url='/mydreams', permanent=False), name='mydreams'),
    url(r'^addtask/(?P<dream_id>[0-9]+)/$','T4CI.views.addtask', name='addtask'),
    url(r'^deletetask/(?P<dream_id>[0-9]+)/$','T4CI.views.deletetask', name='deletetask'),
    url(r'^edittask/(?P<dream_id>[0-9]+)/$','T4CI.views.edittask', name='edittask'),
    url(r'^team/(?P<dream_id>[0-9]+)$', 'T4CI.views.team', name='team'),
    url(r'^addteammember/(?P<dream_id>[0-9]+)/$','T4CI.views.addteammember', name='addteammember'),
    url(r'^deleteteammember/(?P<dream_id>[0-9]+)$', 'T4CI.views.deleteteammember', name='deleteteammember'),
    url(r'^deletedream/(?P<dream_id>[0-9]+)$', 'T4CI.views.deletedream', name='deletedream'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^dream/(?P<dream_id>[0-9]+)/$', 'T4CI.views.dream', name='dream'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)