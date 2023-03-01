import numpy as np

def IsInCollision(x,obc):
    if (x[0] > 20 or x[0] < -20) or \
		   (x[1] > 20 or x[1] < -20):
        return True
    size = 5.0
    s=np.zeros(2,dtype=np.float32)
    s[0]=x[0]
    s[1]=x[1]
    for i in range(0,7):
        collision = True
        for j in range(0,2):
            if abs(obc[i][j] - s[j]) > size/2.0:
                collision = False
                break
        if collision == True:
            return True
    return False
