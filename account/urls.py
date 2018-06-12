from django.conf.urls import url
from . import views

app_name = "account"

urlpatterns = [
    # url(r'^profile/$', views.view_profile, name='view_profile'),
    # url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
     url(r'^(?P<username>[^/]+)/$', views.profile, name='profile'),
     
]
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]