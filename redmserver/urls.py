from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'redeem.views.rules'),
    url(r'^register/(?P<name>.+)/(?P<email>.+)/$', 'redeem.views.register'),
    url(r'^redeem/(?P<name>.+)/(?P<redmcode>.+)/$', 'redeem.views.redeem'),
)
