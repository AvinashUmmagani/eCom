from product.models import Product
Product.objects.all()
mobile = Product.objects.first()
mobile.tag_set
mobile.tag_set.all()
power = Product.objects.second()  
power = Product.objects[2]      
power = Product.objects('2')
qs = Product.objects.all()
mobile = qs.first()
mobile.tag_set
mobile.tag_set.all()
mobile.tag_set.filter(title__iexact='m-obile')
