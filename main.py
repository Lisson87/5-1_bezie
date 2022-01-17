Px = [3,2,2,4]
Py = [1,3,6,8]

def main():
    t = float(input("Введите значение (t): "))

    f = (1 - t)
    THREE = 3

    f3 = f ** 3
    f2 = f ** 2
    t3 = t ** 3
    t2 = t ** 2

    x = f3 * Px[0] + THREE * t * f2 * Px[1] + THREE * t2 * f * Px[2] + t3 * Px[3]
    y = f3 * Py[0] + THREE * t * f2 * Py[1] + THREE * t2 * f * Py[2] + t3 * Py[3]

    print("x = ", x)
    print("y = ", y)


while 1:
    main()