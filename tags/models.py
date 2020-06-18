from django.db import models
from django.db.models.signals import pre_save, post_save
from product.utils import unique_slug_generator
from product.models import Product
from django.urls import reverse

# Create your models here.
class tag(models.Model):
    title = models.CharField(max_length = 150)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, blank = True) 
    def __str__(self):
        return self.title

def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender = tag)