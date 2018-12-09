class ConnectableDevice:
    def __self__(self, internet):
        self.internet = internet
        self.ip_address = self.internet.register(self)
        self.last_id = -1
        self.connections = {}


    # tcp
    def establis_connection(self, ip_address):
        connected_object = self.internet.connect(self.ip_address, ip_address)
        if connect_ip != None:
            connections[ip_address] = connected_object

    # any packet protocol
    def recieve_connect(self, ip_address):
        connected_object = self.internet.recieve_connect(ip_address)
        if connected_object != None:
            connections[ip_address] = connected_object

    def location(self):
        return (0,0)
