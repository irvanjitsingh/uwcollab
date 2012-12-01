from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from auth.views import LandingView, logout
from posts.views import HomeView
import settings


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lunchify.views.home', name='home'),
    # url(r'^lunchify/', include('lunchify.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LandingView.as_view(), name='login'),
    url(r'^logout/?$', logout, name='logout'),
    url(r'^home/?$', HomeView.as_view(), name='home'),
    url("", include('django_socketio.urls')),
    url("", include("chat.urls")),

)

# Path to static assets
media_root = {'document_root': settings.MEDIA_ROOT}
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', media_root),
    # (r'^accounts/login/$', 'django_cas.views.login'),
    # (r'^accounts/logout/$', 'django_cas.views.logout'),
)

urlpatterns += staticfiles_urlpatterns()

