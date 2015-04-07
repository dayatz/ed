from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'core.views.home', name='home'),
    url(r'^login/$', 'core.views.login', name='login'),
    url(r'^logout/$', 'core.views.logout', name='logout'),

    url(r'^admin/', include(admin.site.urls)),
]
