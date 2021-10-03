import numpy as np
import matplotlib.pyplot as plt

def array_of_points_step(n, left_border, right_border):
    points = [[0] * n for k in range(2)]
    step = ((right_border - left_border)/n)
    for i in range(n - 1):
        points[0][i] = step * i
        points[1][i] = function(step * i)
    points[0][n - 1] = right_border
    points[1][n - 1] = function(right_border)
    return points

def array_of_points_cheb(n, left_border, rigth_border):
    points = [[0] * n for k in range(2)]
    c1 = float((left_border + rigth_border)/2)
    c2 = float((rigth_border - left_border)/2)
    for i in range(n):
        a =(((2*i))*np.pi)/(2*n)
        points[0][i] = c1 + c2 * np.cos(a)
        points[1][i] = function(points[0][i])
    return points

def lagranz(points, n, x):
    polynomial = 0
    for k in range(n):
        mult = 1
        point_k = points[0][k]
        for j in range(n):
            point_cur = points[0][j]
            if k != j:
                mult *= ((x - point_cur)/(point_k - point_cur))
        polynomial += mult * points[1][k]
    return polynomial

def graphic(points, n, left_border, rigth_border):

    x = np.linspace(left_border, rigth_border, 1000)
    y_lagranz = [lagranz(points,  n, i) for i in x]
    y = lambda x: function(x)

    plt.subplot(211)
    plt.title(" ")
    plt.title("График полинома и график ошибки")
    plt.plot(x, y(x))
    plt.plot(x, y_lagranz, c='#8f9805')
    plt.scatter(points[0], points[1], c='#d62728')
    plt.grid(True)

    plt.subplot(212)
    plt.plot(x, abs(y_lagranz - y(x)))
    plt.grid(True)

    plt.show()

def graphic_mist(points_step, points_cheb, n, left_border, rigth_border):
    x = np.linspace(left_border, rigth_border, 1000)
    y_lagranz_step = [lagranz(points_step, n, i) for i in x]
    y_lagranz_cheb = [lagranz(points_cheb, n, i) for i in x]
    y = lambda x: function(x)

    plt.subplot(211)
    plt.title(" ")
    plt.title("Равномерный щаг")
    plt.plot(x, abs(y_lagranz_step - y(x)))
    plt.grid(True)

    plt.subplot(212)
    plt.title("Чебышев")
    plt.plot(x, abs(y_lagranz_cheb - y(x)))
    plt.grid(True)

    plt.show()

def function(x):
    return np.sin(x)

def main():
    str1 = input("Write amount of points: ")
    n = int(str1)
    str2 = input("Write left border: ")
    left = float(str2)
    str3 = input("Write rigth border: ")
    right = float(str3)

    points_step = array_of_points_step(n, left, right)
    points_cheb = array_of_points_cheb(n, left, right)
    graphic_mist(points_step, points_cheb, n, left, right)

if __name__ == '__main__':
    main()

