"""
Calculus


- Functions
f(x) = x^2 + 3

- Rise over run
Gradient is a rate of change. For instance if we have a graph of speed over time it's gradient would give us acceleration. 
Second derivative of the speed would be the gradient of the acceleration over time graph which would be a Jerk of the car.

Taking the slop of each point of the function line gives us derivative/gradient of the original function (acceleration/time for speed/time)

Integrals are anti-derivate, speed/time is the anti-derivate of acceleration/time. It's the inverse of the derivate. 


- Definition of derivative
Gradient = rise/run
Gradient = f(x + deltaX) - f(x)/ (x + deltaX) - x which equals to f(x + deltaX) - f(x) / deltaX
Gradient at x, as lim(deltaX) -> 0, equals to f(x + deltaX) - f(x) / deltaX
Using the formula above we come to the conclusion that gradient of a function a* x + b is just a
Power rule, f(x) = a * x^b, f'(x) = a * b * x^(b-1)
Sum rule, f(x) = f1(x) + f2(x), f'(x) = f'1(x) + f'2(x) 


- Differentiation examples & special cases
1. f(x) = 1/x, f'(x) = -1/x^2 -- after applying gradient function above ^
2. f(x) = e^x, where e is Euler's number == 2.71828, f'(x) = e^x
3. f(x) = sin(x), f'(x) = cos(x), f''(x) = -sin(x), f'''(x) = -cos(x), f''''(x) = sin(x)


- Product rule
A(x) = f(x)g(x), A'(x) = f(x)g'(x) + g(x)f'(x)


- Chain rule
h = h(p), p = p(m), dh/dm = dh/dp * dp/dm
f(g(x)), f'(g(x)) * g'(x), df/dg * dg/dx
"""
