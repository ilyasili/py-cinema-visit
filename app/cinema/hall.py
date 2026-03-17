class CinemaHall:
    def __init__(self, number):
        self.number = number

    def movie_session(self, movie_name, customers):
        for i in customers:
            print(f"{movie_name} started in hall number {self.number}")