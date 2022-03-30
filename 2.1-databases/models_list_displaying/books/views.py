from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def show_book(request, dt: datetime):
    template = 'books/book.html'
    books_objects = Book.objects.all()
    book_date = [b_date.pub_date for b_date in books_objects]
    book = Book.objects.get(pub_date=dt)
    get_index = book_date.index(book.pub_date)

    previous = None
    next_p = None
    if get_index == 0:
        previous = None
        next_p = get_index + 1
    elif book.pub_date == book_date[-1]:
        previous = get_index - 1
        next_p = None
    else:
        next_p = get_index + 1
        previous = get_index - 1

    context = {
        'book': book,
        'book_date': book_date,
        'next': next_p,
        'previous': previous,
        'next_date': book_date[next_p],
        'previous_date': book_date[previous],
    }
    return render(request, template, context)
