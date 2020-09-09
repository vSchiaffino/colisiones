import math

def pointPoint(x1, y1, x2, y2):
    """
    Detects the collission between two points.
    
    Parameters:
    p1 = (x1, y1)
    p2 = (x2, y2)
    """
    if (x1 == x2 and y1 == y2):
        return True
    return False

def pointCircle(x, y, cx, cy, r):
    """
    Detects the collission between a point and a circle. 
    
    Parameters:
    p = (x, y)
    
    center = (cx, cy)
    radius = r
    """
    dx = abs(x - cx)
    dy = abs(y - cy)
    d = math.sqrt(dx ** 2 + dy ** 2)
    if d <= r:
        return True
    return False

def circleCircle(cx1, cy1, cx2, cy2, r1, r2):
    """
    Detects the colission between two circles.

    Parameters:
    Circle 1
    center = (cx1, cy1)
    radius = r1

    Circle 2
    center = (cx2, cy2)
    radius = r2
    """
    dx = abs(cx1 - cx2)
    dy = abs(cy1 - cy2)
    d = math.sqrt(dx ** 2 + dy ** 2)
    if d <= r1 + r2:
        return True
    return False

def pointRectangle(rtlx, rtly, rw, rh, px, py):
    """
    Checks colission between a point and a rectangle.

    Parameters:
    RECT
    top-left-point = (rtlx, rtly)
    width = rw
    height = rh
    POINT = (px, py)
    """
    if px >= rtlx and px <= rtlx + rw and py >= rtly and py <= rtly + rh:
        return True
    return False 

def rectangleRectangle(r1tlx, r1tly, r2tlx, r2tly, r1w, r1h, r2w, r2h):
    """
    Checks a colission between two rectangles.

    Parameters:
    RECT1
    top-left-point = (rt1lx, rt1ly)
    width = r1w
    height = r1h
    RECT2
    top-left-point = (rt2lx, rt2ly)
    width = r2w
    height = r2h
    """
    if r1tlx + r1w >= r2tlx and r1tlx <= r2tlx + r2w and r1tly <= r2tly + r2h and r1tly + r1h >= r2tly:
        return True
    return False

def circleRectangle(ccx, ccy, cr, rtlx, rtly, rw, rh):
    """
    Detects the colission between a circle and a rectangle.
    
    Parameters:
    Circle center = (ccx, ccy)
    Circle radius = cr
    Rectangle top-left point = (rtlx, rtly)
    Rectangle width = rw
    Rectangle Height = rh
    """
    testX = ccx
    testY = ccy
    if (ccx < rtlx):
        testX = rtlx
    elif (ccx > rtlx+rw):
        testX = rtlx+rw 
    if (ccy < rtly):
        testY = rtly
    elif (ccy > rtly+rh):
        testY = rtly+rh
    
    dx = abs(ccx - testX)
    dy = abs(ccy - testY)
    d = math.sqrt(dx ** 2 + dy ** 2)
    if d <= cr:
        return True
    return False
    
def linePoint(x1, y1, x2, y2, px, py):
    """
    Detects the colission between a line and a point.
    parameters:
    The line consts about 2 points.
    p1 = (x1, y1)
    p2 = (x2, y2)

    Point = (px, py)
    """
    dtlx = abs(x1 - x2) 
    dtly = abs(y1 - y2) 
    dtl = math.sqrt(dtlx ** 2 + dtly ** 2)

    d1x = abs(x1 - px)
    d1y = abs(y1 - py)
    d1 = math.sqrt(d1x ** 2 + d1y ** 2)
    
    d2x = abs(x2 - px)
    d2y = abs(y2 - py)
    d2 = math.sqrt(d2x ** 2 + d2y ** 2)

    if d1 + d2 == dtl:
        return True

    return False

def lineCircle(x1, y1, x2, y2, cx, cy, cr):
    """
    Detects the colission between a line and a circle.
    Parameters
    First point of the line = (x1, y1)
    Second point of the line = (x2, y2)
    Center point of the circle = (cx, cy)
    Radius of the circle = cr
    """
    inside1 = pointCircle(x1, y1, cx, cy, cr)
    inside2 = pointCircle(x2, y2, cx, cy, cr)
    if inside1 or inside2: return True
    dx = x1 - x2
    dy = y1 - y2
    len = math.sqrt((dx ** 2) + (dy ** 2))

    dot = ( ((cx-x1)*(x2-x1)) + ((cy-y1)*(y2-y1)) ) / (len ** 2)
    closestX = x1 + (dot * (x2-x1))
    closestY = y1 + (dot * (y2-y1))
    onSegment = linePoint(x1,y1,x2,y2, closestX,closestY)
    if not onSegment: return False

    distX = closestX - cx
    distY = closestY - cy
    distance = math.sqrt((distX ** 2) + (distY **2))
    if distance <= cr:
        return True
    return False

def lineLine(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Detects the colission between two lines.
    parameters:
    4 points. 2 for the first line 2 for the second.
    first = (x1, y1), (x2, y2)
    second = (x3, y3), (x4, y4)
    """
    try:
        uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
        uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
        if (uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1):
            intersectionX = x1 + (uA * (x2-x1))
            intersectionY = y1 + (uA * (y2-y1))
            # print(f"({intersectionX},{intersectionY})")
            return True
        return False
    except:
        return False

def lineRectangle(x1, y1, x2, y2, rtlx, rtly, rw, rh):
    """
    Detects if exits a collision between a line and a rectangle.

    Parameters:
    line points: p1 = (x1, y1), p2 = (x2, y2)
    Rectangle top-left point = (rtlx, rtly)
    Rectangle width = rw, rectangle height = rh
    """
    p0x, p0y = rtlx, rtly
    p1x, p1y = rtlx + rw, rtly
    p2x, p2y = rtlx + rw, rtly + rh
    p3x, p3y = rtlx, rtly + rh
    leftLine = lineLine(x1, y1, x2, y2, p0x, p0y, p3x, p3y)
    upLine = lineLine(x1, y1, x2, y2, p0x, p0y, p1x, p1y)
    rightLine = lineLine(x1, y1, x2, y2, p1x, p1y, p2x, p2y)
    bottomLine = lineLine(x1, y1, x2, y2, p3x, p3y, p2x, p2y)
    if leftLine or upLine or rightLine or bottomLine:
        return True
    return False

def polygonPoint(polygon, px, py):
    """
    Detects if exist a colission between a polygon and a point.

    Parameters:
    polygon = list of tuples with 2 values, x and y acording to each point of the polygon
    ex: [(200,100), (400,130), (350,300), (250,300)]
    point = (px, py)
    """
    collision = False
    next = 0
    for current in range(len(polygon)):
        next = current + 1
        if next == len(polygon): next = 0
        vc = polygon[current]
        vn = polygon[next]
        if (((vc[1] >= py and vn[1] < py) or (vc[1] < py and vn[1] >= py)) and (px < (vn[0] - vc[0])*(py-vc[1]) / (vn[1]-vc[1])+vc[0])):
            collision = not collision
    return collision

def polygonCircle(polygon, cx, cy, cr):
    """
    Detects if exist a colission between a polygon and a circle.

    Parameters:
    polygon = list of tuples with 2 values, x and y acording to each point of the polygon
    ex: [(200,100), (400,130), (350,300), (250,300)]
    Circle center point = (cx, cy)
    Circle radius = cr
    """
    next = 0
    if polygonPoint(polygon, cx, cy):
        return True
    for current in range(len(polygon)):
        next = current + 1
        if next == len(polygon): next = 0
        cp = polygon[current]
        np = polygon[next]
        if lineCircle(cp[0], cp[1], np[0], np[1], cx, cy, cr):
            return True
    
    return False

def polygonRectangle(polygon, rtlx, rtly, rw, rh):
    """
    Detects if exist a colission between a polygon and a rectangle.

    Parameters:
    polygon = list of tuples with 2 values, x and y acording to each point of the polygon
    ex: [(200,100), (400,130), (350,300), (250,300)]
    Rectangle top-left point = (rtlx, rtly)
    rectangle width = rw
    rectangle height = rh
    """
    for current in range(len(polygon)):
        next = current + 1
        if next == len(polygon): next = 0
        cp = polygon[current]
        np = polygon[next]
        if lineRectangle(cp[0], cp[1], np[0], np[1], rtlx, rtly, rw, rh):
            return True
    if polygonPoint(polygon, rtlx, rtly): return True
    return False

def polygonLine(polygon, p1x, p1y, p2x, p2y):
    """
    Detects if exist a colission between a polygon and a line.

    Parameters:
    polygon = list of tuples with 2 values, x and y acording to each point of the polygon
    ex: [(200,100), (400,130), (350,300), (250,300)]
    the line const of 2 points, p1 = (p1x, p1y), p2 = (p2x, p2y)
    """
    for current in range(len(polygon)):
        next = current + 1
        if next == len(polygon): next = 0
        cp = polygon[current]
        np = polygon[next]
        if lineLine(cp[0], cp[1], np[0], np[1], p1x, p1y, p2x, p2y):
            return True
    return False

def polygonPolygon(p1, p2):
    """
    Detects if exist a colission between a polygon and a polygon.

    Parameters:
    p1 and p2 = list of tuples with 2 values, x and y acording to each point of the polygon
    """
    for current in range(len(p1)):
        next = current + 1
        if next == len(p1): next = 0
        cp = p1[current]
        np = p1[next]
        if polygonLine(p2, cp[0], cp[1], np[0], np[1]):
            return True
    if polygonPoint(p1, p2[0][0], p2[0][1]):
        return True
    return False
