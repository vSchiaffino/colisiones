import math

def r_sin(a): return math.sin(a)

def r_cos(a): return math.cos(a)

def sin(a): return math.sin(math.radians(a))

def cos(a): return math.cos(math.radians(a))

def atan(a): return math.degrees(math.atan(a))

def partir_mov(mt, ang):
    """
    Descompone un movimiento en movx y movy segun el angulo dado.
    
    Parametros:
    mt = movimiento total
    ang = angulo

    Devuelve una lista de floats que contiene [movx, movy]
    """
    # basicamente divido el movimiento total en movx y movy segun el angulo usando trigonometria.
    movx = sin(ang) * mt
    movy = cos(ang) * mt
    # ahora tengo que ver la direccion del movimiento.
    # divido el angulo en 4 partes
    # !-----------!
    # !  3  !  0  !   
    # !-----!-----!
    # !  2  !  1  !
    # !-----------!
    parte = (ang // 90) % 4
    signo_por_parte = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
    signo = signo_por_parte[parte]
    mov = [signo[0] * abs(movx), signo[1] * abs(movy)]
    return mov

def centro_del_poligono(puntos):
    """
    Dado ciertos puntos de un polígono, devuelve el punto central
    obtenido a través de promedios.
    """
    mid_point_x = 0
    mid_point_y = 0
    for p in puntos:
        mid_point_x += p[0]
        mid_point_y += p[1]
    mid_point_x = mid_point_x / len(puntos)
    mid_point_y = mid_point_y / len(puntos)
    return [mid_point_x, mid_point_y]

def rotar_poligono(puntos, ang):
    """
    Dado cierto angulo, rota el polígono dado en relación a su centro.
    """
    angulo_en_randianes = math.radians(ang)
    mp = centro_del_poligono(puntos)
    for p in puntos:
        x = p[0]
        y = p[1]
        xc = mp[0]
        yc = mp[1]
        # aplico la fórmula matematica
        p[0] = (x - xc) * math.cos(angulo_en_randianes) - (y - yc) * math.sin(angulo_en_randianes)
        p[1] = (x - xc) * math.sin(angulo_en_randianes) + (y - yc) * math.cos(angulo_en_randianes) 
        p[0] += mp[0]
        p[1] += mp[1]
    offset_x = 0
    offset_y = 0
    w = 800
    h = 600
    for p in puntos:
        x = p[0]
        y = p[1]
        if x > w:
            tx = w - x
            if abs(tx) > abs(offset_x):
                offset_x = tx
        if y > h:
            ty = h - y
            if abs(ty) > abs(offset_y):
                offset_y = ty
        if x < 0:
            tx = x
            if abs(tx) > abs(offset_x):
                offset_x = -tx
        if y < 0:
            ty = y
            if abs(ty) > abs(offset_y):
                offset_y = -ty
    for p in puntos:
        p[0] += offset_x
        p[1] += offset_y
    
    return puntos