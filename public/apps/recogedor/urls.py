#! /usr/bin/env python
#-*- encoding:utf-8 -*-

from django.contrib import admin
from django.urls import path, re_path
from apps.recogedor import views as v

app_name = 'module_recogedor'
urlpatterns = [
    # path('regions/', v.get_regions, name="regions"),
    # path('regions/<int:pk>/', v.get_region, name="region"),
    # re_path(r'regions/?$', v.get_regions, name="regions"),
    # re_path(r'regions/(?P<pk>[0-9]+)/?$', v.get_region, name="region"),
    # re_path(r'regions/?$',
    #         v.GetRegions.as_view(), name="regions"),
    # re_path(r'regions/(?P<pk>[0-9]+)/?$',
    #         v.GetRegion.as_view(), name="region"),
    re_path(r'regions/?$',
            v.RegionList.as_view(), name="region_list"),
    re_path(r'regions/(?P<pk>[0-9]+)/?$',
            v.RegionItem.as_view(), name="region_item"),
]
