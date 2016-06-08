from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm

def index(request):
    """
    Get top five categories and top five pages from the database.
    """
    top_categories = Category.objects.order_by('-likes')[:5:]
    top_pages =  Page.objects.order_by('-views')[:5:]
    context_dict = {'categories': top_categories, 'pages': top_pages}

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

        # Add parameters to the context_dict
        context_dict['pages'] = pages
        context_dict['category'] = category
        context_dict['category_name_slug'] = category_name_slug

    except Category.DoesNotExist:
        # If category did not exist, display "no category" message
        context_dict['category'] = None
        #context_dict['pages'] = None
        #context_dict['category_name_slug'] = None

    
    return render(request, 'rango/category.html', context_dict)

def add_category(request):
    """
    Adds a new category to the database via a user-submitted form.
    """
    form = CategoryForm()

    # If user wants to post (submit) the form
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            # save new category to the database
            form.save(commit=True)
            # go back to index after form is submited
            return index(request)
        else:
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    """
    Adds a new page to the database via a user-submitted form.
    """
    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        category = None
        category_name_slug = None

    form = PageForm()

    if request.method == "POST":
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.save()
            return show_category(request, category_name_slug)
        else:
            print(form.errors)
    return render(request, 'rango/add_page.html',
                 {'form': form, 'category': category})

def about(request):
    return render(request, 'rango/about.html')
