from django.db import models

from products.models import Product
from profiles.models import UserProfile


RATING = (
    (1,  "★☆☆☆☆"),
    (2,  "★★☆☆☆"),
    (3,  "★★★☆☆"),
    (4,  "★★★★☆"),
    (5,  "★★★★★"),
)


class ProductReview(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=RATING, default=None)
    review = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name}, {self.user}'

    @property
    def get_rating_range(self):
        '''Returns review rating range'''
        return range(self.rating or 1)

