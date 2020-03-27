from django.urls import path, re_path
from . import views
from serviceProviderApp.views import KitchenUpdate, ProviderRegisterView,registerKitchen
from userModule.views import createMenuItem,createKitchen
from django.conf.urls import url

urlpatterns = [
    re_path(r'^$',views.ProviderRegisterView, name='providersignup'),
    #re_path(r'^$',registerKitchen.as_view(), name='providersignup'),
    re_path(r'^create/$',createKitchen.as_view(),name='kitchenCreate'),
    re_path(r'^(?P<pk>\d+)$',KitchenUpdate.as_view(),name='kitchenUpdate'),
    #url(r'^(?P<pk>\d+)/createMenuItem$', createMenuItem.as_view(), name='createMenuItem'),
    url(r'^createMenuItem$', createMenuItem.as_view(), name='createMenuItem'),
    #url(r'^$', views.product_list, name='product_list'),
    #url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    #url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
