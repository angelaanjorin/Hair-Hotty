from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Wishlist
from .forms import UserProfileForm
from blog.models import Post
from checkout.models import Order
from products.models import Product
from products.utils import products_pagination

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'profile_id': profile.id,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def my_orders(request, profile_id):
    ''' Renders my orders page '''
    profile = get_object_or_404(UserProfile, pk=profile_id)

    orders = profile.orders.all().order_by('-date')
    
    context = {
        'orders': orders,
        'profile_id': profile.id,
    }
    return render(request, 'profiles/my_orders.html', context)



@login_required
def my_wishlist(request, profile_id):
    ''' Renders wishlist page '''
    profile = get_object_or_404(UserProfile, pk=profile_id)
    
    wishlist = Wishlist.objects.filter(user=profile).order_by('-created')
    
    wishlist = products_pagination(request, wishlist, 6)

    context = {
        'wishlist': wishlist,
        'profile_id': profile.id,
    }
    return render(request, 'profiles/wishlist.html', context)


@login_required
def wishlist_add(request, product_id):
    ''' Adds products to favourites, Takes request and product id as pk '''

    profile = request.user.userprofile
    product = get_object_or_404(Product, pk=product_id)
    redirect_url = request.POST.get('redirect_url')

    wishlist, created = Wishlist.objects.get_or_create(
        user=profile, product=product)
    if created:
        messages.success(request, f'{product.name} added to your wishlist')
    else:
        wishlist.delete()
        messages.success(
            request, f'{product.name} removed from your wishlist')

    return redirect(redirect_url)



@login_required
def my_posts(request, profile_id):
    ''' Renders my-posts page '''
    profile = get_object_or_404(UserProfile, pk=profile_id)
    posts = Post.objects.filter(author=profile.user).order_by('-created_on')

    context = {
        'my_posts': my_posts, 
        'profile_id': profile.id,
    }
    return render(request, 'profiles/my_posts.html', context)
