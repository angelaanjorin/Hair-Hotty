from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


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
        


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False,null=True, blank=True)
    stock_amount = models.IntegerField(
        default=1, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    in_stock = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.IntegerField(null=True, blank=True)
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
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
    def product_in_stock(self):
        '''
        Determines if the product is in stock
        based on the stock amount.
        '''
        if self.stock_amount >= 1:
            return True
        else:
            return False

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
        #Set the discount value based on price and sale_price
        self.discount = self.price_discount
        
        #Check for stock staus
        self.in_stock = self.product_in_stock
        
        if not self.on_sale:
            #If there is no sale price then clear it
            self.sale_price = None

        # Update 'has_sizes' field based on ProductSize records
        if self.sizes.exists():
            self.has_sizes = True
        else:
            self.has_sizes = False

        # Recalculate the total stock for the product, considering the sizes.
        if self.has_sizes:
            self.stock_amount = sum(size.stock for size in self.sizes.all())
        else:
            self.stock_amount = 0

        super().save(*args, **kwargs)

