import cv2
import numpy as np

src = cv2.imread("/home/rodion/yuliia0/aboba/cv/trans/my.jpg")
map_x = np.zeros((src.shape[0], src.shape[1]), dtype=np.float32)
map_y = np.zeros((src.shape[0], src.shape[1]), dtype=np.float32)

def update_map(ind, map_x, map_y):
    if ind == 0:
        for i in range(map_x.shape[0]):
            for j in range(map_x.shape[1]):
                if j > map_x.shape[1]*0.25 and j < map_x.shape[1]*0.75 and i > map_x.shape[0]*0.25 and i < map_x.shape[0]*0.75:
                    map_x[i,j] = 2 * (j-map_x.shape[1]*0.25) + 0.5
                    map_y[i,j] = 2 * (i-map_y.shape[0]*0.25) + 0.5
                else:
                    map_x[i,j] = 0
                    map_y[i,j] = 0
    elif ind == 1:
        for i in range(map_x.shape[0]):
            map_x[i,:] = [x for x in range(map_x.shape[1])]
        for j in range(map_y.shape[1]):
            map_y[:,j] = [map_y.shape[0]-y for y in range(map_y.shape[0])]
    elif ind == 2:
        for i in range(map_x.shape[0]):
            map_x[i,:] = [map_x.shape[1]-x for x in range(map_x.shape[1])]
        for j in range(map_y.shape[1]):
            map_y[:,j] = [y for y in range(map_y.shape[0])]
    elif ind == 3:
        for i in range(map_x.shape[0]):
            map_x[i,:] = [map_x.shape[1]-x for x in range(map_x.shape[1])]
        for j in range(map_y.shape[1]):
            map_y[:,j] = [map_y.shape[0]-y for y in range(map_y.shape[0])]

update_map(0, map_x, map_y)
dst = cv2.remap(src, map_x, map_y, cv2.INTER_LINEAR)
cv2.imshow("Remap 1", dst)

update_map(1, map_x, map_y)
d = cv2.remap(src, map_x, map_y, cv2.INTER_LINEAR)
cv2.imshow("Remap 2", d)

update_map(2, map_x, map_y)
ds = cv2.remap(src, map_x, map_y, cv2.INTER_LINEAR)
cv2.imshow("Remap 3", ds)

update_map(3, map_x, map_y)
dstq = cv2.remap(src, map_x, map_y, cv2.INTER_LINEAR)
cv2.imshow("Remap 4", dstq)
cv2.waitKey(0)