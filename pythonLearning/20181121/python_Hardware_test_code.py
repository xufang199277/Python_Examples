# test code
import python_Hardware_learning
a = python_Hardware_learning.wave(formula = "sin(x)",period = 2)
b = python_Hardware_learning.wave(formula = ".5 * sin(2*x)",period = 2)
c = python_Hardware_learning.wave(formula = "sin(x) + .5 * sin(2*x)",period = 2)
c.plot(maxY = 1.2, pixHeight = 300, pixWidth = 600, title = "Sin(x)", others=[a,b])

# c.plot(maxY = 1.2, pixHeight = 200, title = "Sin(x) plus .5*Sin(2*x)", others=[b])