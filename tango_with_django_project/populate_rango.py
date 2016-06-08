import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


"""
Populate creates lists of dictionaries containing the pages that we want
to add into each category.
Then, create a dictionary of those dictionary to iterate over them and 
fill our models with the data.
"""

def populate():

    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/'},
        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/'},
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial'},]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'http://docs.djangoproject.com/en/1.9/intro/tutorial01/'},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/'},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/'},]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://www.bottlepy.org/docs/dev'},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org'},]

    categories = {'Python': 
                    {'pages': python_pages, 'views': 128, 'likes': 64},
                  'Django': 
                    {'pages': django_pages, 'views': 64, 'likes': 32},
                  'Other Frameworks': 
                    {'pages': other_pages, 'views': 32, 'likes': 16}}

    # Populate the database
    for cat, cat_data in categories.items():
        c = add_category(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])

    # Print out all categories 
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {} - {}".format(str(c), str(p)))


def add_page(category, title, url, views=0):
    p = Page.objects.get_or_create(category=category, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_category(name, views, likes):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c


if __name__ == '__main__':

    print('Starting Rango population script...')
    populate()

