from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def products_pagination(request, products, results):
    ''' Handles Pagination '''
    paginator = Paginator(products, results)
    page_number = request.GET.get('page')

    try:
        return paginator.page(page_number)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)

    return products