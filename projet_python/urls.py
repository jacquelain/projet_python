from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('acceuil.views',
    # Examples:
    # url(r'^$', 'projet_python.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
#     url(r'^visite/$', 'visite', name='visite'),
#     url(r'^administration/$', 'administration', name='administration'),
#     url(r'^prof/$','prof'),
#     url(r'^titre_cours/$', 'titre_cours', name='titre_cours'),
#     url(r'^code_cours/$', 'code_cours', name='code_cours'),
#     url(r'^descriptif_cours/$', 'descriptif_cours', name='descriptif_cours'),
)
