from obstaculo import Obstaculo
from copy import deepcopy
from trigonometria import rotar_poligono, partir_mov, centro_del_poligono

class Hb(Obstaculo):
    def __init__(self, puntos):
        super().__init__("poly")
        # ---- defino los puntos del poligono de la hitbox ----
        # ancho = 50
        # alto = 50
        # medio = 30
        # self.puntos = [[0, 0], [ancho, 0], [ancho, medio], [ancho // 2, alto], [0, medio]]
        # alto1 = 10
        # alto2 = 5
        # alto = 60
        # ancho = 40
        # anchodiv = 10
        # self.puntos = [[0, 0],[anchodiv, -alto1],[anchodiv * 2, -alto1 - alto2],[anchodiv * 3, -alto1],[ancho, 0],[ancho, alto],[0, alto]]
        self.puntos = puntos
        for p in self.puntos:
            p[0] += 50
            p[1] += 50
        self.ang = 0
        # -------------------------------------------------- debug -------------#
        mid_point_x = 0                                                         #
        mid_point_y = 0                                                         #
        for p in self.puntos:                                                   #
            mid_point_x += p[0]                                                 #
            mid_point_y += p[1]                                                 # 
        mid_point_x = mid_point_x / len(self.puntos)                            #
        mid_point_y = mid_point_y / len(self.puntos)                            #
        mp = [mid_point_x, mid_point_y]                                         #
        i = 0                                                                   #
        for p in self.puntos:                                                   #
            print(f"p{i}: ({p[0] - mp[0]}, {p[1] - mp[1]}), ")                  #
            i += 1                                                              #
        # print(mp)                                                             #
        for p in self.puntos:                                                   #
            #print(f"diff = ({mp[0] - p[0]}, {mp[1] - p[1]})")                  #
            pass                                                                #
        # -------------------------------------------------- debug -------------#

    def mover(self, movt, obstaculos):
        # copio por si hay colision
        ang_viejo = deepcopy(self.ang)
        puntos_viejos = deepcopy(self.puntos)
        ang_viejo_2 = deepcopy(self.ang)
        puntos_viejos_2 = deepcopy(self.puntos)
        ang_a_usar = self.ang
        if movt < 0:
            ang_a_usar = ang_a_usar + 180
        mov_tentativo = partir_mov(movt, ang_a_usar)
        # hago el mov en dos partes
        # en x
        self._mover_puntos([mov_tentativo[0], 0])
        if not self._check_colissions(obstaculos, ang_viejo, puntos_viejos):
            # estuvo bien, entonces backupeo
            ang_viejo_2 = deepcopy(self.ang)
            puntos_viejos_2 = deepcopy(self.puntos)
        else:
            ang_viejo_2 = deepcopy(self.ang)
            puntos_viejos_2 = deepcopy(self.puntos)
        # en y
        self._mover_puntos([0, mov_tentativo[1]])
        if not self._check_colissions(obstaculos, ang_viejo_2, puntos_viejos_2):
            pass

    def _mover_puntos(self, mov):
        for p in self.puntos:
            p[0] += mov[0]
            p[1] += mov[1]
    
    def rotar(self, ang, obstaculos):
        # hago un backup por si colisiona
        ang_viejo = deepcopy(self.ang)
        puntos_viejos = deepcopy(self.puntos)
        # roto
        self.puntos = rotar_poligono(self.puntos, ang)
        self.ang += ang
        robots = []
        for o in obstaculos:
            if not o.tipo == "line":
                robots.append(o)
        if self._check_colissions(robots, ang_viejo, puntos_viejos):
            pass

    def get_center(self):
        return centro_del_poligono(self.puntos)

    def _check_colissions(self, obstaculos, ang_viejos, puntos_viejos):
        re = False
        for o in obstaculos:
            if o.check_colission(self):
                re = True
        if re:
            # printprint("Colission")
            self.ang = ang_viejos
            self.puntos = puntos_viejos
        return re