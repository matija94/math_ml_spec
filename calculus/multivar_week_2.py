"""
- Variables, constants & context
Multivaraiate systems(multiple variables)


Differentiating variable which is multiplied by constants just leaves constants
m = zy + xhy
dm/dh = xy --> this is partial derivative, because there was more than one variable in the function



- Differentiating with anything
partial derivative = pD
Total derivative
df(x,y,z)/dt = pDf/pDx * dx/dt + pDf/pDy * dy/dt + pDf/pDz * dz/dt


- Jacobian
Put a results of partial derivates in row vector which when given 
parameters of the function points to steepest slope of the function 
f(x,y,z) = [pDf/pDx, pDf/pDy, pDf/pDz] => points to steepest slope for any x,y,z input

Jocobian vector has greatest maginitude at the point where the function is the most steep

Jacobian describes the gradient of a multivariable system. 
Length of Jacobian matrix is propotional to local steepness.

- Hessian
Extends from Jacobian. Collects all second derivates of the function parameters into a matrix.

Hessian can be used to tell if we're dealing with minimum or maximum, when the Jacobian is 0

The power of the Hessian is, firstly, that if its determinant is positive, we know we are dealing with either a max or a min.
Secondly, we then just look at the first term, which is sitting at the top left-hand corner of the Hessian. 
If this guy is also positive, we know we've got a min, as in this particular case. Whereas, if it's negative, we've got a max.


- Multivaraiate chain rule
f(x(u(t))), where x and u are vector valued functions while t is scalar
df/dt = [pDf/pDx1, pDf,pDx2] * [[pDx1/pDu1, pDx1/pDu2],[pDx2/pDu1, pDx2/pDu2]] * [du1/dt, du2/dt]
df/dt = pDf/pDx * pDx/pDu * du/dt


- Neural nets, feedforward & backpropagation
Feed forward equations:
a(n) = sigma(z(n))
z(n) = W(n) @ a(n-1) + b(n)
where W and b are paremeters, W is a vector of weights connecting neurons while b is bias scalar associated to every neuron
C = (a(n) - y)^2
cost function, a(n) is the output layer, y is the desired outcome


In case of network with 2 layers
z(0) = W(0) @ x + b(0); x is the input, each succeding layer's input is previous layer output
a(0) = sigma(z(0)) 

z(1) = W(1) @ a(0) + b(1)
a(1) = sigma(z(1))
C = (a(1) - y)^2 

To find the ideal weights and biases which produce desired outcome we have to calculate Jacobian vectors
Jacobian vectors contain partian derivates for multivariate system, such as nerutal net, which has two unknown variables W and b
We need to calculate partial derivates for all weights and biases, in all layers.

Calculate parital derivates for W(1) and b(1)
J(1) = [dC/da(1) * da(1)/dz(1) * dz(1)/dw(1), dC/da(1) * da(1)/dz(1) * dz(1)/db(1)]
Calculate parital derivates for W(0) and b(0)
J(0) = [dC/da(1) * da(1)/dz(1) * dz(1)/da(0) * da(0)/dz(0) * dz(0)/dw(0),dC/da(1) * da(1)/dz(1) * dz(1)/da(0) * da(0)/dz(0) * dz(0)/db(0)]
"""
