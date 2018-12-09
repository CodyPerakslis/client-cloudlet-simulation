from movement import Movement


class Client:
    def __init__(self, x, y):
        self.location_api = Movement()

    def next_time(self, unit=1):
        self.location_api.next_time(unit)

    def location(self):
        return self.location_api.location()
