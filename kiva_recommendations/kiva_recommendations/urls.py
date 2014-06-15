from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

@csrf_exempt
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kiva_recommendations.views.home', name='home'),
    # url(r'^kiva_recommendations/', include('kiva_recommendations.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
		url(r'^auth/kiva_request/', 'kiva_recommendations.authentication.kiva_request', name='kiva'),
		url(r'^auth/kiva_access/', 'kiva_recommendations.authentication.kiva_access', name='kiva'),

		url(r'^loan_list', 'kiva_recommendations.data.loan_list', name='loan_list')
)
