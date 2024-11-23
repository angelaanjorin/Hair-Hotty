from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg

from products.models import Product

from .models import Review
from .forms import ReviewForm


# Create your views here.
@login_required
def add_review(request, product_id):
    '''A view that handels adding a review
        Logged in Users Only (redirects to log in).
        Adds new review to database.
    '''
    # Sets product based on product_id
    product = get_object_or_404(Product, pk=product_id)

    # confirms user
    user = request.user.userprofile

    # Handles Form Submission
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = user
            review.save()

            # Updates product rating on product object
            reviews = product.reviews.all()
            review_count = reviews.count()

            if review_count > 0:
                avg_rating = round(reviews.aggregate(Avg('rating'))['rating__avg'], 1)
            else:
                avg_rating = 0

            product.rating = avg_rating
            product.save()

            request.session['show_bag_summary'] = False
            messages.success(request, 'Review added successfully.')
        else:
            messages.error(
                request, 'Star Ratings missing, please try again.'
            )
        return redirect(reverse('product_detail', args=[product.id]))

    # Handles View Rendering
    else:
        form = ReviewForm()

    # Sets page template
    template = 'products/product_detail.html'

    # Sets current product & form content
    context = {
        'form': form,
        'product': product,
        'avg_rating': product.rating,
        'review_count': product.reviews.count(),
        'review' : product.reviews.all(),
    }

    return render(request, template, context)
