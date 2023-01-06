import random
from pylab import sin, array, plot,show
from numpy import pi

from LeastSquares import leastSquares3exc5
from Askisi5 import Exercise5
from Askisi6 import Exercise6
from Askisi7 import Exercise7

def exercise5():
    exc = Exercise5()
    x = [random.uniform(-3.14,3.14) for i in range(200)]
    x.sort()
    # Approx. pi/12
    print("\tApproximation of pi/12\n")
    print("Actual: %.5f\n"%(sin(pi/12)))
    print("Lagrange: %.5f"%(exc.lagrange(pi/12)))
    print("Error: %.7f\n"%(sin(pi/12)-exc.lagrange(pi/12)))
    print("Splines: %.5f"%(exc.splines(pi/12)))
    print("Error: %.7f\n"%(sin(pi/12)-exc.splines(pi/12)))
    print("LeastSquares(3): %.5f"%(leastSquares3exc5(pi/12, exc.points)))
    print("Error: %.7f\n"%(sin(pi/12)-leastSquares3exc5(pi/12, exc.points)))
    # max e
    ysin = [sin(xi) for xi in x]
    ylagrange = [exc.lagrange(xi) for xi in x]
    yDiffLagrange = [ysin[i]-ylagrange[i] for i in range(200)]
    ysplines = [exc.splines(xi) for xi in x]
    yDiffSplines = [ysin[i]-ysplines[i] for i in range(200)]
    yleastSquares = [leastSquares3exc5(xi, exc.points) for xi in x]
    yDiffLeastSquares = [ysin[i]-yleastSquares[i] for i in range(200)]
    ##plots
    #plot(x,yDiffLagrange,'r')
    #show()
    #plot(x,yDiffSplines,'m')
    #show()
    #plot(x,yDiffLeastSquares,'b')
    #show()
    print("Max Lagrange error: ", max(abs(array(yDiffLagrange))))
    print("Max splines error: ", max(abs(array(yDiffSplines))))
    print("Max least squares error: ", max(abs(array(yDiffLeastSquares))))
    #ylg = [exc.lagrange(x[i]) for i in range(30)]
    #ysp = [exc.splines(x[i]) for i in range(30)]
    #yls = [exc.leastSquares3(x[i]) for i in range(30)]
    #plot(x, ylg, 'r')
    #plot(x, ysp, 'm')
    #plot(x, yls, 'g')
    #show()

def exercise6():
    exc = Exercise6()
    exc.TrapezoidRule()
    exc.Simpson()

def exercise7():
    exc = Exercise7()
    exc.predictions()
    #y = [point[1] for point in exc.pointsDPA]
    #y2 = [point[1] for point in exc.pointsDTX]
    #plot(exc.x, y, 'r')
    #show()
    #plot(exc.x, y2, 'b')
    #show()


def main():
    exercise5()
    #exercise6()
    #exercise7()

main()