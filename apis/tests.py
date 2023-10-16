import pytest
from django.urls import reverse
from rest_framework import status
from books.models import Book

@pytest.mark.django_db
def test_api_listview(client):
    book = Book.objects.create(
        title="Django for APIs",
        subtitle="Build web APIs with Python and Django",
        author="William S. Vincent",
        isbn="9781735467221",
    )

    response = client.get(reverse("book_list"))
    assert response.status_code == status.HTTP_200_OK
    assert Book.objects.count() == 1
    assert str(book) in str(response.content)

