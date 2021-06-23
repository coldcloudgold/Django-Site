from django.core.paginator import Paginator


def paginate(data, request, count=10):
    paginator = Paginator(data, count)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    context = {
        "page_obj": page,
        # "paginator": paginator,
    }
    return context
