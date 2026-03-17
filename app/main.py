from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    for i in customers:
        cd = CinemaBar()
        cd.sell_product(i.get('name'), i.get('food'))

    cd = CinemaHall(hall_number)
    cd.movie_session(movie, customers)

    for i in customers:
        cd = Customer(i.get('name'), i.get('food'))
        cd.watch_movie(movie)

    print(f'"{movie}" ended.')

    cd = Cleaner(cleaner_name)
    cd.clean_hall(hall_number)
    pass

cinema_visit(customers, hall_number, cleaner_name, movie)
