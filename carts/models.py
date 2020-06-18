from decimal import Decimal
from django.db import models
from django.conf import settings 
from product.models import Product
from ec import views as ec_views
from django.db.models.signals import pre_save, post_save, m2m_changed
import math
# Create your models here.
User = settings.AUTH_USER_MODEL
class CartManager(models.Manager):
    def new_or_get(self, req):
        cart_id = req.session.get("cart_id",None)
        qs = self.get_queryset().filter(id = cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if req.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = req.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new_cart(user=req.user)
            new_obj = True
            req.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new_cart(self, user = None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user = user_obj)



class Cart(models.Model):
    user = models.ForeignKey(User, null = True, blank = True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank = True)
    subtotal = models.DecimalField(default = 0.00,max_digits = 100, decimal_places = 2)
    total = models.DecimalField(default = 0.00,max_digits = 100, decimal_places = 2)
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    objects = CartManager()
    def __str__(self):
        return str(self.id)

def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()
        total = 0
        for x in products:
            total += x.price
        if instance.subtotal!= total:
            instance.subtotal = total
            instance.save()
m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)

def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal>0:
        instance.total = float(instance.subtotal) + float(instance.subtotal)*float(0.18)
    else:
        instance.total = 0.00
pre_save.connect(pre_save_cart_receiver, sender=Cart)
