"""huitraining URL Configuration

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
import huiweb.views
import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', huiweb.views.index),
    url(r'^details(?P<DetailsId>\d+)$', huiweb.views.details),
    url(r'^login$',huiweb.views.account_login),
    url(r'^index.html$',huiweb.views.index),
    url(r'^edit_plan$', huiweb.views.edit_ini),
    url(r'^pdf_upload$', huiweb.views.pdf_upload),
    url(r'^user_query$', huiweb.views.user_query),
    url(r'^pdf_path$', huiweb.views.pdf_path),
    url(r'^plan_details(?P<DetailsId>\d+)$', huiweb.views.plan_details),
    url(r'^user_manage$', huiweb.views.user_manage),
    url(r'plan_query$', huiweb.views.plan_query),
    url(r'plan_query(?P<digital_id>\d+)$', huiweb.views.plan_query_details),
]

