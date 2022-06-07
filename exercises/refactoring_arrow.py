"""
Refactor the code below. Try go get the functions' bodies
as close to the left side as possible (only one indentation deep).
"""
import pytest

available_movies = {
    "Tomorrow Never Dies": {"id": "tomorrow_never_dies", "quality": "IMAX", "genre": "Action"},
    "Robin Hood": {"id": "robin_hood", "quality": "regular", "genre": "Adventure"},
    "Pulp Fiction": {"id": "pulp_fiction", "quality": "regular", "genre": "Crime"},
}


def invoice(movie, tickets):
    amount = 0
    movie_in_available_movies = False
    for title in available_movies:
        if title == movie:
            movie_in_available_movies = True
            if tickets != 0:
                if available_movies[movie]["quality"] == "IMAX":
                    price = 12
                    if tickets >= 5:
                        discount = 10
                    else:
                        discount = 0
                else:
                    price = 10
                    if tickets >= 5:
                        discount = 10
                    else:
                        discount = 0
            else:
                raise ValueError("Cannot calculate price for 0 tickets")
    if movie_in_available_movies is False:
        raise LookupError("Movie not available")
    else:
        total_amount = amount + (tickets * price) - discount
        return total_amount


# Test suite
def test_invoice_without_discount():
    assert invoice("Pulp Fiction", 1) == 10


def test_invoice_with_discount():
    assert invoice("Pulp Fiction", 6) == 50


def test_invoice_imax_movie():
    assert invoice("Tomorrow Never Dies", 3) == 36


def test_invoice_0_tickets():
    with pytest.raises(ValueError):
        invoice("Pulp Fiction", 0)


def test_invoice_unknown_movie():
    with pytest.raises(LookupError):
        invoice("Unknown Movie", 5)
