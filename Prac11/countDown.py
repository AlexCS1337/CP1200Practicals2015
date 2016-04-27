__author__ = 'Smoo'


def countDown(n):
    if n <= 0:
        countUp(4)
    else:
        print(n)
        countDown(n - 1)

def countUp(n):
    if n <= 0:
        print("LIFTOFF!")
    else:
        countUp(n - 1)
        print(n)

countDown(4)