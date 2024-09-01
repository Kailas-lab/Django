from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'book_form.html', {'form': form})

# Update
def book_update(request, title):
    try:
        book = Book.objects.get(title=title)
    except Book.DoesNotExist:
        return redirect('book_list')

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'book_form.html', {'form': form})

# Read
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, title):
    try:
        book = Book.objects.get(title=title)
    except Book.DoesNotExist:
        return redirect('book_list')
    return render(request, 'book_detail.html', {'book': book})

# Delete
def book_delete(request, title):
    try:
        book = Book.objects.get(title=title)
    except Book.DoesNotExist:
        return redirect('book_list')

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})
