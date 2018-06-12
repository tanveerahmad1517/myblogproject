"""myblogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .views import SearchView
from myblogproject import views
from django.contrib.auth.views import LoginView

from django.conf import settings
from django.conf.urls import include, url 
# from search import views as search_views
from filebrowser.sites import site

from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/filebrowser/', site.urls),
    path('tinymce/', include('tinymce.urls')),

    path('', include('posts.urls')),
    path('account/', include('account.urls')),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('search/', SearchView.as_view(), name='search'),
    # url(r'^autocomplete/$',
    #     search_views.get_autocomplete_suggestions, name='autocomplete'),
    # url(r'^search/$', search_views.search, name='search'), 
   

]
urlpatterns += [
    path('', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
