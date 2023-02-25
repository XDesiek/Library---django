from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Comment
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.contrib.postgres.search import SearchVector
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm,CreateUserForm,PaginatorChangePageForm,SearchForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from taggit.models import Tag
from django.db.models import Count
# Create your views here.

# class BookListView(ListView):
#     queryset = Book.objects.all()
#     context_object_name = "booklist" # jak sie nazywa w template'ah
#     paginate_by = 1
#     template_name = "library/book/list.xhtml"




# def login(request):
#     return render(request,request, "library/login.xhtml")



# @require_POST
# def create_user(request):
#     user = None
#     # Comentarz został opublikowany
#     form = CreateUserForm(data=request.POST)
#     if form.is_valid():
#         user.save()

#     return render(request, "library/createuser.xhtml",{'user': user,'form': form})













        







def book_list(request, tag_slug=None):
    book_list = Book.objects.all()
    tag = None
    
    searchform = SearchForm()
    query = None
    results = [] 
    if 'query' in request.GET:
        searchform = SearchForm(request.GET)
        if searchform.is_valid():
            query = searchform.cleaned_data['query'] 
            results = Book.objects.annotate(search=SearchVector('title', 'desc')).filter(search=query)    


    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        book_list = book_list.filter(tags__in=[tag])
        


    paginator = Paginator(book_list, 5)
    paginatorform = PaginatorChangePageForm()
    if paginatorform.is_valid():page_number  = paginatorform.cleaned_data['page']
    else:page_number = request.GET.get('page', 1)


    # testy paginatora
    try:books = paginator.page(page_number)
    except PageNotAnInteger:books = paginator.page(1)
    except EmptyPage:books = paginator.page(paginator.num_pages)

    return render(request,
                 'library/book/list.xhtml',
                 {'books': books,
                  'tag': tag,
                  "paginatorform":paginatorform,
                  'searchform': searchform,
                   'query': query,
                   'results': results})


def book_detail(request, year, month, day, book):
    book = get_object_or_404(
        Book,
        slug=book,
        publication_date__year=year,
        publication_date__month=month,
        publication_date__day=day,
    )
    comments= book.comments.filter(active=True)
    form = CommentForm()
        # Lista podobnych postów
    book_tags_ids = book.tags.values_list('id', flat=True)
    similar_books = Book.objects.filter(tags__in=book_tags_ids)\
                                  .exclude(id=book.id)
    similar_books = similar_books.annotate(same_tags=Count('tags'))\
                                 .order_by('-same_tags','-rating','-publication_date')[:4]

    return render(request, "library/book/detail.xhtml",{"book":book,
                                                        "form":form,
                                                        "comments":comments,
                                                        "similar_books":similar_books
                                                        })



def book_share(request, book_id):
    # Retrieve post by id
    book = get_object_or_404(Book, id=book_id)
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            book_url = request.build_absolute_uri(
                book.get_absolute_url())
            subject = f'{cd["name"]} recommends you read {book.title}'
            message = f'Read {book.title} at {book_url}\n\n' \
                      f'{cd["name"]}\'s comments: {cd["comments"]}'
            send_mail(subject, message, 'tony.j.kaminski@gmail.com',
                      [cd['to']],fail_silently=False)
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'library/book/share.xhtml', {'book': book,
                                                    'form': form,
                                                    'sent': sent})







# ...
@require_POST
def book_comment(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    comment = None
    # Comentarz został opublikowany
    form = CommentForm(data=request.POST)
    if form.is_valid():
	  # Utworzenie obiektu Comment bez zapisania go do bazy danych
        comment = form.save(commit=False)
        # przypsanie postu do komentarza
        comment.book = book
        # zapisanie komentarza
        comment.save()
    return render(request, 'library/book/comment.xhtml',
                           {'book': book,
                            'form': form,
                            'comment': comment})

