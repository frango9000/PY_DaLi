from lib.geometry.Circle import Circle
from lib.geometry.Rectangle import Rectangle


def ex01():
    print("Welcome to Python")
    print("Learning Java Now")
    print("Programming is fun")


def ex02():
    loops = 5
    while loops > 0:
        print("I love Python")
        loops -= 1


def ex04():
    print("a   a^2  a^3 a^4")
    loop = 1

    while loop < 5:
        print("{:} {:4} {:4} {:4}".format(loop ** 1, loop ** 2, loop ** 3, loop ** 4))
        loop += 1


def ex05():
    print(((7.5 * 6.5) - (4.5 * 3)) / (47.5 - 5.5))


def ex06():
    loop = 1
    sum = 0
    while loop < 10:
        sum += loop
        loop += 1
    print(sum)


def ex08():
    circle = Circle(6.5)
    print(circle.getArea())


def ex09():
    print(Rectangle(5.3, 8.6).getArea())


ex09()
