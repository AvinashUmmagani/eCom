from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404
from carts.models import Cart
from analytics.mixins import ObjectViewMixin
from .models import Product
# Create your views here.
class productFeaturedListView(ListView):
    template_name = 'productListView.html'
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()


class productFeaturedDetailView(ObjectViewMixin,DetailView):
    template_name = 'productFeaturedDetailView.html'    
    queryset = Product.objects.featured()
    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(featured = True)



class productListView(ListView):
    queryset = Product.objects.all()
    template_name = 'productListView.html'
    def get_context_data(self,*args, **kwargs):
        context = super(productListView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)###
        context["cart"] = cart_obj
        return context

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(productListView,self).get_context_data(*args, **kwargs)
        return context
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
# def productlist_view(req):
#     queryset = Product.objects.all()
#     context = {'object_list':queryset}
#     return render(req,'productListView.html',context)



class productDetailView(ObjectViewMixin,DetailView):
    queryset = Product.objects.all()
    template_name = 'productDetailView.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(productDetailView,self).get_context_data(*args, **kwargs)
        # print(context)
        return context
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        qs = Product.objects.filter(id = pk)
        instance = Product.objects.get_by_id(id=pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk = pk)

class productDetailSlugView(ObjectViewMixin,DetailView):
    queryset = Product.objects.all()
    template_name = 'productDetailView.html'

    # def get_context_data(self, *args, **kwaargs):
    def get_context_data(self,*args, **kwargs):
        context = super(productDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)###
        context["cart"] = cart_obj
        return context
    

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        qs = Product.objects.filter(slug = slug)
        instance = Product.objects.get(slug=slug)
        if instance is None:
            raise Http404("Product doesn't exist")
        #object_viewed_signal.send(instance.__class__, instance=instance,request=request)
        return instance


def productdetail_view(req, pk):
    # instance = Product.objects.get(pk=pk)
    # queryset = Product.objects.all()
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('No product')
    #     raise Http404("Product doesn't exist")
    
    qs = Product.objects.filter(id = pk)
    instance = Product.objects.get_by_id(id=pk)
    if instance is None:
        raise Http404("Product doesn't exist")
    # print(instance)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
        # raise Http404("Product doesn't exist")
    context = {'object':instance}
    return render(req,'productDetailView.html',context)