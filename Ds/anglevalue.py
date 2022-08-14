def triangle(x,y):
    T_angle = 180-(x+y)
    return T_angle    
    
def squareshape (x,y,z):
    S_angle= 360 - (x+y+z)
    return S_angle 
def prntgram (x,y,z,i)  :
    P_angle =540-(x+y+z+i)
    return P_angle 
def heptagon (a,x,y,z,i,j):
    H_angle = 900 - (x+y+z+a+i+j)
    return H_angle
def octagon (a,b,x,y,z,i,j):
    O_angle = 1080 -(x+y+z+a+i+j)
    return O_angle