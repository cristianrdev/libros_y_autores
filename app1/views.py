from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author
# Create your views here.
#lista todo los libros
def index(request):

    context = {
        "todos_los_libros": Book.objects.all()
    }
    return render(request, 'index.html', context)

# guarda/crea un nuevo libro

def save_book(request):
    new_book = Book.objects.create(
        title= request.POST['titulo'],
        description= request.POST['descripcion'],
        )
    return redirect('/')
# lista el detalle del libro cuando es GET, Al libro se le asocia un autor cuando es POST
def books_detail(request, num):
 
    if request.method == 'GET':


        libro_buscado = Book.objects.get(id=num)
        autor_asociado_al_libro = libro_buscado.authors.all()

        context = {
            "libro": Book.objects.get(id=num),
            "autores": Author.objects.all(),
            "autores_del_libro": autor_asociado_al_libro,
            
        }
        print("ahora es GET-----------------------------")
        return render(request, 'books.html', context)
    else:
        this_author = Author.objects.get(id=request.POST['autores'])
        this_book = Book.objects.get(id=num)

        this_author.books.add(this_book)
        print(request.POST['autores'])
        print("ahora es POST-----------------------------")
        return redirect('/books/'+ str(num))

# lista todos los autores
def authors(request):
    context = {
        "todos_los_autores": Author.objects.all()
    }
    
    return render(request, 'authors.html', context)
# guarda/crea un nuevo libro
def save_author(request):
    new_author = Author.objects.create(
    first_name= request.POST['nombre'],
    last_name= request.POST['apellido'],
    notes= request.POST['notas'],
        )
    return redirect('/authors')


# lista el detalle del autor cuando es GET, Al autor se le asocia un libro cuando es POST
def authors_detail(request, num):

    if request.method == 'GET':

        autor_buscado = Author.objects.get(id=num)
        libro_asociado_al_autor = autor_buscado.books.all()
        context = {
            "author": Author.objects.get(id=num),
            "libros": Book.objects.all(),
            "libros_del_autor": libro_asociado_al_autor,
            
        }
        return render(request, 'author_detail.html', context)
        print("ahora es GET-----------------------------")
    else:
        this_book = Book.objects.get(id=request.POST['libro'])
        this_author = Author.objects.get(id=num)

        this_book.authors.add(this_author)
        print(request.POST['libro'])
        print("ahora es POST-----------------------------")
        return redirect('/authors/'+ str(num))
