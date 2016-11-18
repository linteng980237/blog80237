from django.shortcuts import render

from book.models import Book


def book(request):
    '''
    Render the article page
    '''
    return render(request, 'book/book.html')