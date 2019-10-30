"""sskmlt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from authentication.views import UserLogin,dashboard,UserView,users,view_userdetails,register,create_lorry,update_lorry,lorries,consignees,consigners,create_consigner,create_consignee,entries,register,accountentry,report,download_report,userlogout
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',UserLogin.as_view()),
    url(r'^register/',register),
    url(r'^$',dashboard),
    url(r'^dashboard/',dashboard),
    url(r'^report/',report),
    url(r'^entries/',entries),
    url(r'^lorry/(?P<id>[0-9]*)[/]*$',update_lorry),
    url(r'^create_lorry/',create_lorry),
    url(r'^download_report/',download_report),
    url(r'^lorries/',lorries),
    url(r'^consignees/',consignees),
    url(r'^consigners/',consigners),
    url(r'^create_consigner/(?P<id>[0-9]*)[/]*$',create_consigner),
    url(r'^create_consignee/(?P<id>[0-9]*)[/]*$',create_consignee),
    url(r'^accountentry/(?P<pk>[0-9]*)[/]*$',accountentry),
    url(r'^logout/',userlogout),


    # consignees,consigners,create_consigner,create_consignee

    # url(r'^ppv-record/(?P<date>[0-9]*)[/]*$',ppv_record),
    # url(r'^logout/',))
    # url(r'users_list/',show_users, name='users_list'),
]
