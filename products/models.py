from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from decimal import Decimal


class ProductSize(models.Model):
    """
    Model to manage sizes and stock amounts for products.
    """
    SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]

    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='sizes'
    )
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    stock = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)]
    )

    class Meta:
        unique_together = ('product', 'size')  # Ensure unique size for each product

    def __str__(self):
        return f"{self.product.name} - {self.size} (Stock: {self.stock})"
        

class PrimaryCategory(models.Model):
    """
    Categories that are unique to a product, like hair_wigs, hair_extensions, etc.
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Primary Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class SpecialCategory(models.Model):
    """
    Optional categories like deals, new_arrivals, and best_collections.
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Special Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    primary_category = models.ForeignKey(
        PrimaryCategory,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='products'
    )
    special_categories = models.ManyToManyField(
        SpecialCategory,
        blank=True,
        related_name='products'
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False,null=True, blank=True)
    stock_amount = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    in_stock = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.IntegerField(null=True, blank=True)
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def price_discount(self):
        '''
        Calculate discount based on new price
        '''
        if self.sale_price:
            discount = ((self.price - self.sale_price) / self.price) * 100
            return round(discount)
        else:
            return None

    @property
    def stock_details(self):
        """
        Returns stock details. 
        For products with sizes, returns size-wise stock dictionary.
        """
        if self.has_sizes and self.sizes.exists():
            return {size.size: size.stock for size in self.sizes.all()}
        return {"stock": self.stock_amount}


    @property
    def product_price(self):
        '''
        Returns the price of item based on
        if item is on sale
        '''
        if self.on_sale and self.sale_price < self.price:
            return self.sale_price
        return self.price

    def save(self, *args, **kwargs):
        # If the product is on sale, calculate the sale_price if a discount is provided
        if self.on_sale:
            if self.discount is not None:
                # Calculate the sale price based on the discount percentage but convert self.discount to a decimal
                self.sale_price = round(self.price * (Decimal(1) - Decimal(self.discount)/ 100))
            elif self.sale_price is None:
                # If no discount or sale_price is provided, raise an error
                raise ValueError("Either sale_price or discount must be provided if the product is on sale.")

        # Ensure discount is calculated correctly when sale_price is manually set
        if self.sale_price and self.sale_price < self.price:
            self.discount = round((1 - self.sale_price / self.price) * 100)

        # Reset sale_price and discount if not on sale
        if not self.on_sale:
            self.sale_price = None
            self.discount = None

        # Compute stock and in_stock status
        if self.sizes.exists():
            self.stock_amount = sum(size.stock for size in self.sizes.all())
            self.has_sizes = True
        else:
            self.has_sizes = False
            self.stock_amount = max(self.stock_amount, 0)

        self.in_stock = self.stock_amount > 0

        # Save the product
        super().save(*args, **kwargs)
