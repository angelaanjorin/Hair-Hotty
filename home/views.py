from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def index(request):
    """" A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    ''' Renders About us page '''
    return render(request, 'home/about.html')


def contact(request):
    """
    Renders the contact page
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(
                request, "Your message has been sent successfully!")

            return redirect('home')
        else:
            messages.error(
                request,
                "There was an error with your submission. Please try again.")
    else:
        form = ContactForm()

    return render(
        request,
        "home/contact.html", {
            'form': form
        }
    )


def privacy_policy(request):
    ''' Renders Privacy Policy page '''
    return render(request, 'home/privacy_policy.html')


def faq_page(request):
    ''' Renders FAQ page  '''
    return render(request, 'home/faq_page.html')