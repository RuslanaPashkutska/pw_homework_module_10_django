from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from .utils import get_mongodb


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.get_page(page)
    context = {
        "quotes": quotes_on_page,
        "has_prev": quotes_on_page.has_previous(),
        "has_next": quotes_on_page.has_next(),
        "prev_page": quotes_on_page.previous_page_number() if quotes_on_page.has_previous() else None,
        "next_page": quotes_on_page.next_page_number() if quotes_on_page.has_next() else None,
    }

    return render(request, "quotes/index.html", context=context)

