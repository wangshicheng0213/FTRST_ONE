"""DDDatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from message.views import getform
from message.views import getHome
from message.views import getPPINetwork
from message.views import getCoExAnalysis
from message.views import getExPaAnalysis
from message.views import getDownload
from message.views import getManual
from message.views import getSearchGene
from message.views import search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^Home/$', getHome,name = 'go_Home'),
    url(r'^form/$',getform,name = 'go_form'),
    url(r'^$', getHome,name = 'go_Home'),
    url(r'^PPINetwork/$', getPPINetwork,name   = 'go_PPINetwork'),
    url(r'^ExPaAnalysis/$', getExPaAnalysis,name = 'go_ExPaAnalysis'),
    url(r'^CoExAnalysis/$', getCoExAnalysis,name = 'go_CoExAnalysis'),
    url(r'^Download/$', getDownload,name = 'go_Download'),
    url(r'^Manual/$', getManual,name = 'go_Manual'),
    url(r'^SearchGene/$', getSearchGene,name = 'go_SearchGene'),
    url(r'^SearchGene1/$', search, name = 'go_SearchGene1'),
]
