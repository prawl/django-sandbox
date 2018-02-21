from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from . import view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # The first argument is an empty string, so any request that doesn't match anything go to the hello world view
    url(r'^courses/', include('courses.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', view.hello_world),
]

 # Check if we're in dev and then check if we have a static path and include them
urlpatterns += staticfiles_urlpatterns()
