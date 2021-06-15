from django.shortcuts import render, redirect

# other imports
from .models import Book
from .models import Author

# Create your render views here.
def index(request):
    print("In index route")

    context = {
    	"all_the_books": Book.objects.all()  #list of "book" objects
    }

    return render(request, "index.html", context)

def create_book(request):
    print("In create books route")

    Book.objects.create(
    title=request.POST["title"],
    description=request.POST["description"],
    )

    return redirect('/')

def specific_book_info(request, book_id):
    print("In specific book info route")

    context = {
        "specific_book": Book.objects.get(id=book_id),
        "authors": Book.objects.get(id=book_id).authors.all(),
        "all_the_authors": Author.objects.all(),
    }

    return render(request, "specific_book_info.html", context)

def append_authors(request, book_id):
    print("In append authors route")
    
    # option = Author.objects.get(id = request.POST['select_author'])
    # Book.objects.get(id = book_id).authors.add(option)
    
    # return redirect(f'/specific_book_info/{book_id}') 
    return redirect("/")   




def authors(request):
    print("In authors route")
    context = {
        "all_the_authors": Author.objects.all()
    }

    return render(request, "authors.html", context)


def create_author(request):
    print("In create author route")

    Author.objects.create(
    first_name=request.POST["first_name"],
    last_name=request.POST["last_name"],
    notes=request.POST["notes"],
    )

    return redirect('/authors')

def specific_author_info(request, author_id):
    print("In specific author info route")

    context = {
        "specific_author": Author.objects.get(id=author_id),
        "books": Author.objects.get(id=author_id).books.all(),
        "all_the_books": Book.objects.all(),
    }

    return render(request, "specific_author_info.html", context)

def append_books(request, author_id):
    
    option = Book.objects.get(id = request.POST['select_book'])
    Author.objects.get(id = author_id).books.add(option)
    
    return redirect(f'/specific_author_info/{author_id}') 

