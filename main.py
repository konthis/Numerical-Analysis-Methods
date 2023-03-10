import random
from pylab import sin, array, plot,show, legend
from numpy import pi

from LeastSquares import leastSquares3Solve
from Interp import Interpolation
from Integral import IntegralSolve
from Prediction import Prediction

def interp():
    exc = Interpolation()
    x = [random.uniform(-3.14,3.14) for i in range(200)]
    x.sort() # x0<x1<...<xn-1
    # Approx. pi/12
    print("\tApproximation of pi/12\n")
    print("Actual: %.5f\n"%(sin(pi/12)))
    print("Lagrange: %.5f"%(exc.lagrange(pi/12)))
    print("Error: %.7f\n"%(sin(pi/12)-exc.lagrange(pi/12)))
    print("Splines: %.5f"%(exc.splines(pi/12)))
    print("Error: %.7f\n"%(sin(pi/12)-exc.splines(pi/12)))
    print("LeastSquares(3): %.5f"%(leastSquares3Solve(pi/12, exc.points)))
    print("Error: %.7f\n"%(sin(pi/12)-leastSquares3Solve(pi/12, exc.points)))
    # max e
    ysin = [sin(xi) for xi in x]
    ylagrange = [exc.lagrange(xi) for xi in x]
    yDiffLagrange = [ysin[i]-ylagrange[i] for i in range(200)]
    ysplines = [exc.splines(xi) for xi in x]
    yDiffSplines = [ysin[i]-ysplines[i] for i in range(200)]
    yleastSquares = [leastSquares3Solve(xi, exc.points) for xi in x]
    yDiffLeastSquares = [ysin[i]-yleastSquares[i] for i in range(200)]
    #plots
    plot(x,yDiffLagrange,'r', label="Lagrange")
    plot(x,yDiffSplines,'m', label="Splines")
    plot(x,yDiffLeastSquares,'b', label="Least Squares(3)")
    legend(loc='upper right')
    show()
    print("Max Lagrange error: ", max(abs(array(yDiffLagrange))))
    print("Max splines error: ", max(abs(array(yDiffSplines))))
    print("Max least squares error: ", max(abs(array(yDiffLeastSquares))))

def integral():
    exc = IntegralSolve()
    exc.trapezoidRule()
    exc.simpson()

def pred():
    exc = Prediction()
    exc.predictions()

def main():
    interp()
    integral()
    pred()

main()