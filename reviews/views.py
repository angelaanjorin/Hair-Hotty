from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from products.models import Product

from .forms import ProductReviewForm
from .models import ProductReview


# Create your views here.
@login_required
def add_review(request, product_id):
    '''A view that handels adding a review'''

    product = get_object_or_404(Product, pk=product_id)
    user = request.user.userprofile
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = user
            review.save()
            messages.success(request, 'Review added successfully.')
        else:
            messages.error(
                request, 'Something went wrong. Please fill in the form again'
            )
        return redirect(reverse('product_detail', args=[product.id]))

    # Handles View Rendering
    else:
        form = ProductReviewForm()

    # Sets page template
    template = 'reviews/add_review.html'

    # Sets current product & form content
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
