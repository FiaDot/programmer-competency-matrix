from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProgrammerCompetencyMatrix.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^survey/$', 'survey.views.main'),
    url(r'^survey/submit$', 'survey.views.submit'),
    url(r'^survey/(\d+)/$', 'survey.views.user'),
)
