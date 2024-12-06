from django.db import models
from django.core.validators import (
    MaxValueValidator, MinValueValidator
)
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg

from products.models import Product
from profiles.models import UserProfile


class Review(models.Model):
    """ Review Model """

    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews"
    )
    rating = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ],
        default=0,
        blank=False,
        null=False
    )
    review = models.TextField(
        max_length=500
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.product.name

    @property
    def get_rating_range(self):
        """Returns review rating range"""
        return range(self.rating)


# Signal to update product rating when a review is added or edited
@receiver(post_save, sender=Review)
def update_product_rating_on_save(sender, instance, **kwargs):
    product = instance.product
    reviews = product.reviews.all()
    product.rating = round(
        reviews.aggregate(
             Avg('rating'))['rating__avg'], 1)if reviews.exists() else 0
    product.save()


# Signal to update product rating when a review is deleted
@receiver(post_delete, sender=Review)
def update_product_rating_on_delete(sender, instance, **kwargs):
    product = instance.product
    reviews = product.reviews.all()
    product.rating = round(
        reviews.aggregate(
             Avg('rating'))['rating__avg'], 1)if reviews.exists() else 0
    product.save()
