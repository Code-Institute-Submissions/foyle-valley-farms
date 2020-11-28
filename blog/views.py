from django.shortcuts import render


# Create your views here.
# https://djangocentral.com/adding-pagination-with-django/


def blog(request):
    
    return render(request, 'blog/blog.html')
