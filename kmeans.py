import matplotlib.pyplot as plt
from math import floor
import numpy as np
import random
import warnings

warnings.filterwarnings("ignore")

def generate_random_points(data_points, size):
    return np.floor(np.random.rand(2, data_points) * size)

def generate_random_centroids(k,size):
    return np.floor(np.random.rand(2, k) * size), np.random.rand(k, 3)

def generate_average(all_points, colours, centroids_x, centroids_y):
    a= []
    b = []
    for i in range(len(colours)):
        summ_x = 0
        summ_y = 0
        count = 0
        for j in all_points:
            if (j[2] == colours[i]).all():
                summ_x += j[0]
                summ_y += j[1]
                count += 1
        a.append(floor(summ_x/count))
        b.append(floor(summ_y/count))

    return np.array(a), np.array(b)




#you can change these parameters

size = 1000 # size of plot
k=3 # number of classes
data_points = 100 #number of data points


x, y = generate_random_points(data_points, size)
centroids, colours = generate_random_centroids(k, size)
all_points = []
for i in range(0, len(x)):
    all_points.append([x[i], y[i], ''])

centroids_x, centroids_y = centroids[0], centroids[1]
plt.plot(x, y, 'ro')
for i in range(0, 10):
    print(centroids_x, centroids_y)
    for i in range(0, len(centroids_x)):
        plt.plot(centroids_x[i], centroids_y[i], 'ro', c=colours[i], marker="X")

    for i in all_points:
        mini = 100000000
        new_colour = ""
        for j in range(0, len(centroids_x)):
            dist = np.linalg.norm(np.array([i[0], i[1]]) - np.array([centroids_x[j], centroids_y[j]]))
            if dist < mini:
                i[2] = colours[j]
                mini = dist
        
    for i in range(0, len(all_points)):
        plt.plot([all_points[i][0]], [all_points[i][1]], 'ro', c=all_points[i][2])
    plt.pause(0.1)

    centroids_x_new, centroids_y_new = generate_average(all_points, colours, centroids_x, centroids_y)
    
    for i in range(len(centroids_x_new)):
        plt.arrow(centroids_x[i], centroids_y[i], centroids_x_new[i] - centroids_x[i], centroids_y_new[i] - centroids_y[i], head_width = 30, width = 0.05, head_length=30)
       
    
    if((centroids_x == centroids_x_new).all() and (centroids_y == centroids_y_new).all()):
        break
        
    centroids_x = centroids_x_new
    centroids_y = centroids_y_new
#plt.show()
for i in range(len(colours)):
    count = 0
    for j in all_points:
            if (j[2] == colours[i]).all():
                count += 1
    print("There are " + str(count) + " in " + str(i) + " cluster with centroid at (" + str(centroids_x[i]) + ", " + str(centroids_y[i]) + ")")
