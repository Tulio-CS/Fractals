import math
import matplotlib.pyplot as plt
from random import choice


n_points = 1000


#Criando o triangulo Base
triangle_size = 100

point_a = (0,0)
point_b = (triangle_size,0)
point_c = (triangle_size / 2 , triangle_size * math.sqrt(3) / 2)

plt.scatter(point_a[0],point_a[1], s = 0.8, color = "#FFD700")
plt.scatter(point_b[0],point_b[1], s = 0.8, color = "#FFD700")
plt.scatter(point_c[0],point_c[1], s = 0.8, color = "#FFD700")

points = [point_a,point_b,point_c]




def new_point(point_1,point_2):
    """Funcao que calcula o ponto medio entre dois pontos
    Tuple, Tuple -> Tuple"""
    x0,y0 = point_1
    x1,y1 = point_2
    new_x = (x1 + x0) / 2
    new_y = (y1 + y0) / 2
    return (new_x, new_y)

def loop(num_points):
    """Funcao loop que criara o triangulo de sierpinski
    int -> None"""
    current = new_point(point_a,point_b)
    plt.scatter(current[0],current[1],s = 0.8, color = "#FFD700")
    for i in range(num_points):
        i = choice(points)
        new = new_point(current,i)
        print(new)
        plt.scatter(new[0],new[1],s = 0.8, color = "#FFD700")
        current = new


if __name__ == "__main__":
    loop(n_points)
    plt.title("Sierpinski Triangle")
    plt.show()





