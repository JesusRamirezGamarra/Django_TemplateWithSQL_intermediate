"""proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings

from blog.views import homepage, search, allposts, post, postlist, dona , contact, embrace,about
from django.conf.urls.static import static

urlpatterns = [
    path("", homepage, name="homepage"),
    path("homepage/", homepage, name="homepage"),
    path("post/<slug>/", post, name="post"),
    path("postlist/<slug>/", postlist, name="postlist"),
    path("posts/", allposts, name="allposts"),
    path("search/", search, name="search"),
    path("dona/", dona, name="dona"),
    path("contact/", contact, name="contact"),
    path("embrace/", embrace, name="embrace"),
    path('about/', about,name = 'about' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
