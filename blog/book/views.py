from django.shortcuts import render

from book.models import Book

def book(request):
    '''
    Render the book page
    '''
    book = Book.objects.all()
    itemsList = []
    for book in book:
        items = [book] 
        itemsList.append(items)
    context = {'itemsList':itemsList}
    return render(request, 'book/book.html', context)
