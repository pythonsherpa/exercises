"""
Refactor the code below. Try go get the functions' bodies
as close to the left side as possible (only one indentation deep).
"""
movies = {
    "tomorrow_never_dies": {"name": "Tomorrow Never Dies", "genre": "Action"},
    "robin_hood": {"name": "Robin Hood", "genre": "Adventure"},
    "pulp_fiction": {"name": "Pulp Fiction", "genre": "Crime"},
}


def invoice(movie, tickets):
    amount = 0
    for title in movies:
        if title == movie:
            if tickets != 0:
                if movie not in movies:
                    raise LookupError("Movie not available")
                else:
                    if movies[title]["genre"] == "Action":
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
    total_amount = amount + (tickets * price) - discount
    return total_amount


print(invoice("pulp_fiction", 6))
