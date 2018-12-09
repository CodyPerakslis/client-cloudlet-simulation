

class Movement:
    def __init__(self):
        self.x = 0
        self.y = 0

    def next_time(self, unit=1):
        self.x += unit
        self.y += unit

    def location(self):
        return (self.x, self.y)
