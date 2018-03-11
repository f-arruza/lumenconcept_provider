from django.conf.urls import url, include

from .views import (ProviderViewSet, CategoryViewSet, RequirementViewSet,
                    SupportViewSet, CalificationViewSet, schema_view)

api_url_patterns = [
    url(r'^categories/$', CategoryViewSet.as_view({
                                                   'get': 'list',
                                                   'post': 'create',
                                                  }), name='category-list'),
    url(r'^categories/(?P<pk>[0-9]+)$', CategoryViewSet.as_view({
                                                   'get': 'retrieve',
                                                   'put': 'update',
                                                   'patch': 'partial_update',
                                                   'delete': 'destroy'
                                                  }), name='category'),
    url(r'^requirements/$', RequirementViewSet.as_view({
                                                       'get': 'list',
                                                       'post': 'create',
                                                       }), name='requirement-list'),
    url(r'^requirements/(?P<pk>[0-9]+)$', RequirementViewSet.as_view({
                                                                     'get': 'retrieve',
                                                                     'put': 'update',
                                                                     'patch': 'partial_update',
                                                                     'delete': 'destroy'
                                                                     }), name='requirement'),
    url(r'^providers/$', ProviderViewSet.as_view({
                                                 'get': 'list',
                                                 'post': 'create',
                                                 }), name='provider-list'),
    url(r'^providers/code/(?P<code>[\w-]+)$', ProviderViewSet.as_view({
                                                         'get': 'retrieve_code'
                                                         }), name='provider-retrieve'),
    url(r'^providers/(?P<pk>[0-9]+)$', ProviderViewSet.as_view({
                                                             'get': 'retrieve',
                                                             'put': 'update',
                                                             'patch': 'partial_update',
                                                             'delete': 'destroy'
                                                             }), name='provider'),
    url(r'^supports/$', SupportViewSet.as_view({
                                               'get': 'list',
                                               'post': 'create',
                                              }), name='support-list'),
    url(r'^supports/(?P<pk>[0-9]+)$', SupportViewSet.as_view({
                                                               'get': 'retrieve',
                                                               'put': 'update',
                                                               'patch': 'partial_update',
                                                               'delete': 'destroy'
                                                              }), name='support'),
    url(r'^califications/$', CalificationViewSet.as_view({
                                               'get': 'list',
                                               'post': 'create',
                                              }), name='calification-list'),
    url(r'^califications/(?P<pk>[0-9]+)$', CalificationViewSet.as_view({
                                                               'get': 'retrieve',
                                                               'put': 'update',
                                                               'patch': 'partial_update',
                                                               'delete': 'destroy'
                                                              }), name='calification'),
]

urlpatterns = [
    url(r'^api/v1/', include(api_url_patterns)),
    url(r'^', schema_view),
]
