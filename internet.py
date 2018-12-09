from math_equations import distance

class Internet:
    def __init__(self):
        self.ips = []
        self.last_ip = -1

    def register(self, object):
        self.last_ip += 1
        ip = self.last_ip
        self.ips[ip] = object
        return ip

    def latency(dist, data):
        # data in bytes, distance in meters, result in ms
        return 100 + data * distance / 1000


    def tcp_handshake(connect_ip, connectee_ip):
        dist = distance(self.ips[connect_ip], self.ips[connectee_ip])
        return


    # tcp
    def connect(self, connector_ip, connectee_ip):
        self.tcp_handshake(connect_ip, connectee_ip)
        if ip_address in self.ips:
            return self.ips[ip_address]
        else:
            return None
