from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer

customers = [{"name": "Bob", "food": "Coca-cola"},
             {"name": "Alex", "food": "popcorn"}]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_instances = []

    for customer in customers:
        cd = Customer(customer.get("name"), customer.get("food"))
        customer_instances.append(cd)

        CinemaBar.sell_product(product=cd.food, customer=cd)

    ch = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    ch.movie_session(movie, customer_instances, clean)
