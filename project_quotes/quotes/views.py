from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

# Create your views here.
# from .utils import get_mongodb
from .models import Quote, Author, Tag
from .forms import QuoteForm, AuthorForm, TagForm

from django.contrib.auth.decorators import login_required


def main(request, page=1):
    # db = get_mongodb()
    # quotes = db.quotes.find()
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={"quotes": quotes_on_page})


def show_author(request, author_id):
    # print(author_id)
    # pk = author_id
    author = Author.objects.get(pk=author_id)
    # author = get_object_or_404(Author, pk)
    print(author.fullname, type(author))

    return render(request, 'quotes/show_author.html', context={"author": author})


# def detail(request, note_id):
#     note = get_object_or_404(Note, pk=note_id)
#     return render(request, 'noteapp/detail.html', {"note": note})


def viewing_tag(request, tag_name):
    print(tag_name)
    id_quotes_from_tag = []
# -------------------------------------------------------------------------------------------------

    # pk = author_id
    # author = Author.objects.get(pk=author_id)
    # # author = get_object_or_404(Author, pk)
    # print(author.fullname, type(author))
    #
    # return render(request, 'quotes/show_author.html', context={"author": author})


# @login_required
def add_quote(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():

            form.save()
            # new_note = form.save()
            #
            # choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            # for tag in choice_tags.iterator():
            #     new_note.tags.add(tag)

            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/add_quote.html', {"tags": tags, 'form': form})

    return render(request, 'quotes/add_quote.html', {"tags": tags, 'form': QuoteForm()})

    # if request.method == 'POST':
    #     form = QuoteForm(request.POST)
    #     if form.is_valid():
    #         # new_quote = form.save()
    #         form.save()
    #         return redirect(to="quotes:home")
    #     else:
    #         return render(request, "quotes/add_quote.html",
    #                       context={"form": QuoteForm(), "message": "Form not valid"})
    # return render(request, "quotes/add_quote.html", context={"form": QuoteForm()})


# @login_required
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/add_tag.html', {'form': form})

    return render(request, 'quotes/add_tag.html', {'form': TagForm()})


# @login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/add_author.html', {'form': form})

    return render(request, 'quotes/add_author.html', {'form': AuthorForm()})
