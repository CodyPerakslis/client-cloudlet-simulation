from client import Client
from cloudlet import Cloudlet
from server import Server

class Simulation:
    def __init__(self, iterations=10):
        self.iterations = iterations
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def build_from_yaml(self, location):
        pass

    def add_items(self, items):
        self.items.extend(items)

    def run_simulation(self):
        for i in range(self.iterations):
            for item in self.items:
                item.next_time()
                if type(item) == Client:
                    print(item.location())




if __name__ == "__main__":
    s = Simulation()
    s.add_items([Client(0,0), Cloudlet(1,1), Server(0,0)])
    s.run_simulation()
