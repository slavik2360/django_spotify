# Python
from typing import Any

# Django
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render


def index(request: WSGIRequest) -> HttpResponse:
    # Example of Function Based View (FBV)
    albums: QuerySet[Album] = Album.objects.all()
    context: dict[str, QuerySet[Any]] = {
        'albums': albums
    }
    return render(
        request,
        'main/index.html',
        context
    )
