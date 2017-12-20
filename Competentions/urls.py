"""Standarts URL Configuration

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
from . import views

urlpatterns = [
    url(r'^test/', views.test),
    url(r'^test2/', views.test2),
    url(r'^test3/', views.test3),
    url(r'^userCompetentions/', views.userCompetentions),
    url(r'^educationalStandarts/', views.educationalStandartsView),
    url(r'^test5/', views.test5),
    url(r'^getStandart/', views.getStandartAjax),
    url(r'^getCustomCompetentionList/', views.getCustomCompetentionListAjax),
    url(r'^getSimpleViewStandart/', views.getSimpleViewStandartAjax),
    url(r'^addCustomCompetention/', views.addCustomCompetentionListAjax),
    url(r'^updateCustomCompetentionList/', views.updateCustomCompetentionListAjax),
    url(r'^addCompetentionToCustomCompetentionList/', views.addCompetentionToCustomCompetentionList),
    url(r'^addCustomCompetentionListAjax/', views.addCustomCompetentionList),
    url(r'^deleteCustomCompetentionList/', views.deleteCustomCompetentionListAjax),
    url(r'^getEducationalStandart/', views.getEducationalStandartAjax),
]
