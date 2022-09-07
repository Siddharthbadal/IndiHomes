from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from django.utils.text import slugify



@receiver(post_save, sender=Product)
def add_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug  = slugify(instance.name)
        instance.slug = slug 