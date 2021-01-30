import math

def calculate_distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
def distance(node1,node2):
    x1 = node1.pos_x
    y1 = node1.pos_y
    x2 = node2.pos_x
    y2 = node2.pos_y
    return calculate_distance(x1,y1,x2,y2)
    

    