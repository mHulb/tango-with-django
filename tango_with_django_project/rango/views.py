from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

def index(request):
    """
    Query the database for a complete list of ALL categories that are stored.
    Order those categories by the number of likes, in descendnig order.
    Extract the top 5 of those categories (if less than 5 available, get all).
    Place a list of the top 5 into the context_dict dictionary and pass
    it to the template engine to render.
    """
    top_categories = Category.objects.order_by('-likes')[:5:]
    context_dict = {'categories': top_categories}

    return render(request, 'rango/index.html', context=context_dict)


def show_category(request, category_name_slug):
    """
    Create a context dictionary which we can pass to the 
    template rendering engine.
    """
    context_dict = {}

    try:
        
        # Is there a category that has the given slug?
        # If none is found, .get wil raise an exception.
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all pages from that category as a list
        pages = Page.objects.filter(category=category)

        # Add this list of pages to the context_dict
        context_dict['pages'] = pages
        # Additionally, we will add the category itself to the
        # context_dict, to verify that it exists afterwards.
        context_dict['category'] = category

    except Category.DoesNotExist:
        # If category did not exist, display "no category" message
        context_dict['category'] = None
        context_dict['pages'] = None

    
    return render(request, 'rango/category.html', context_dict)


def about(request):
    return render(request, 'rango/about.html')
