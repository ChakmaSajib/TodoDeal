# helpers.py  module provides a function to assign task as an parameter into it 
# instead of copying and pasting the same code

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def page_records(request, list, num):
    paginator = Paginator(list, num)

    # get the page parameter from the query string
    # if page parameter is available get() method will return empty string
    page = request.GET.get('page')

    try:
        # Create Page object for the give page
        page = paginator.page(page)
    except PageNotAnInteger:
        # if page parameter in the query string is not available, return the first page 
        page = paginator.page(1)
    except EmptyPage:
        # if the value of the page parameter exceeds num_pages then return the last page    
        page = paginator.page(paginator.num_pages)


    return page







