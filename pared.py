from obstaculo import Obstaculo


class Pared(Obstaculo):
    def __init__(self, p1x, p1y, p2x, p2y):
        super().__init__("line")
        self.p1x = p1x
        self.p1y = p1y
        self.p2x = p2x
        self.p2y = p2y

    def print(self, s):
        pass
