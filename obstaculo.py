from colisiones import polygonPolygon, polygonLine

class Obstaculo():
    def __init__(self, tipo):
        self.tipo = tipo
        # esto lo pongo para q no joda pylint
        self.puntos = ""
        self.p1x = 0
        self.p1y = 0
        self.p2x = 0
        self.p2y = 0

    def check_colission(self, obs):
        if self == obs:
            return False
        if obs.tipo == "poly" and self.tipo == "poly":
            if polygonPolygon(self.puntos, obs.puntos):
                return True
        elif obs.tipo == "poly" and self.tipo == "line":
            if polygonLine(obs.puntos, self.p1x, self.p1y, self.p2x, self.p2y):
                return True
        elif obs.tipo == "line" and self.tipo == "poly":
            if polygonLine(self.puntos, obs.p1x, obs.p1y, obs.p2x, obs.p2y):
                return True
        
        return False