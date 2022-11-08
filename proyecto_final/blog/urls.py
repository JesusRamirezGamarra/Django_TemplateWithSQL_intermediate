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
from django.urls import path,re_path
from django.conf import settings
from django.views.static import serve

from blog.views import homepage, search, allposts, post, postlist, dona , contact, embrace, about, AddPostView, AllPostView_list,allPostView,Create_UserPostColaborator,Read_UserPostColaborator,Update_UserPostColaborator,Delete_UserPostColaborator,login,registrar,perfil,perfil_editar,Password_editar,Logout


from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
import random

result =  lambda a=1,b=2: str(random.randint(a,b)) +'.jpg'

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),    
    # path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    # path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path("", homepage, name="homepage"),
    path("homepage/", homepage, name="homepage"),
    path("post/<str:slug>/", post, name="post"),
    path("postlist/<str:slug>/", postlist, name="postlist"),
    path("posts/", allposts, name="allposts"),
    path("search/", search, name="search"),
    path("dona/", dona, name="dona"),
    path("contact/", contact, name="contact"),
    path("embrace/", embrace, name="embrace"),
    path('about/', about,name = 'about' ),
    path('add_post_colaborator/', AddPostView.as_view(), name='add_post_colaborator'),
    path('all_post_colaborator/', AllPostView_list.as_view(), name='all_post_colaborator'),    
    path('all_post_percolaborator/<str:slug>', allPostView, name='all_post_percolaborator'),  
    
    #CRUD
    path('post_colaborator/create/', Create_UserPostColaborator.as_view(), name='create_post_colaborator'),   
    path('post_colaborator/read/', Read_UserPostColaborator.as_view(), name='read_post_colaborator'),   
    path('post_colaborator/update/<int:pk>/', Update_UserPostColaborator.as_view(), name='update_post_colaborator'),   
    path('post_colaborator/delete/<int:pk>/', Delete_UserPostColaborator.as_view(), name='delete_post_colaborator'),   
    
    
    path("login/", login, name="login"),
    path("registrar/", registrar, name="registrar"),
    #path("logout",Logout,name="logout"),
    path("logout",LogoutView.as_view(template_name="private/logout.html"),{  'result': {'image': result(1,20)} },name="logout"),
    path("perfil/", perfil, name="perfil"),
    path("perfil/editar/", perfil_editar, name="perfil_editar"),
    path("password/editar/", Password_editar.as_view(),name="password_editar"),
    
    
]


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
# else:
#     urlpatterns += url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT})
#     urlpatterns += url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})

