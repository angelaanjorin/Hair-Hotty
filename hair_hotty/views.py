from django.core.exceptions import PermissionDenied
from django.shortcuts import render

'''
Error Handling
'''


def handler404(request, exception):
    '''
    Render 404 page
    '''
    return render(request, '404.html', status=404)


def handler500(request):
    '''
    Render 500 page
    '''
    return render(request, '500.html', status=500)


def handler403(request, exception):
    '''
    Render 403 page
    '''
    if isinstance(exception, PermissionDenied):
        return render(request, '403.html', status=403)
    else:
        return render(request, '500.html', status=500)