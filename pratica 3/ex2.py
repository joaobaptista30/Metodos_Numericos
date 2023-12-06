import math


def f(x):
    return math.sin(x)-(x**2)

pontos=[0.2,0.3,0.5]
x=0.4


def p2(x):  #forma a padeiro
    soma=0

    soma+=(((x-0.3)*(x-0.5)*f(0.2))/((0.2-0.3)*(0.2-0.5)))

    soma+=(((x-0.2)*(x-0.5)*f(0.3))/((0.3-0.2)*(0.3-0.5)))

    soma+=(((x-0.2)*(x-0.3)*f(0.5))/((0.5-0.2)*(0.5-0.3)))

    print(f'p2= {soma:.7f}')

p2(0.4)

