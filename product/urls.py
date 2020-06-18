from django.conf.urls import url
from . import views as product_views

urlpatterns = [
    
    url(r'^productList/$', product_views.productListView.as_view(),name = 'list'),
    #url(r'^productDetail2/(?P<pk>\d+)/$', product_views.productdetail_view),
    #url(r'^productDetail/(?P<pk>\d+)/$', product_views.productDetailView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', product_views.productDetailSlugView.as_view(),name = 'detail'),
    #url(r'^productFeaturedDetail/(?P<pk>\d+)/$', product_views.productFeaturedDetailView.as_view()),
    #url(r'^productFeaturedList/$', product_views.productFeaturedListView.as_view())
]

