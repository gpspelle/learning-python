class Perceptron:
    def __init__(self, w1, w2, bias):
        self.w1 = w1;
        self.w2 = w2;
        self.bias = bias;

    def calculate(self, x1, x2): 
        if self.w1 * x1 + self.w2 * x2 + self.bias > 0:
            self.output  = 1;
        else:
            self.output = 0;

# Initialize all perceptrons
l11 = Perceptron(-2, -2, 3) 
l21 = Perceptron(-2, -2, 3)
l22 = Perceptron(-2, -2, 3)
l23 = Perceptron(-2, -2, 3)
l31 = Perceptron(-2, -2, 3)

# Reading input
x1, x2 = map(int, input("Entre com dois bits (0, 1): ").split())
 
l11.calculate(x1, x2)
l21.calculate(x1, l11.output)
l22.calculate(l11.output, x2)
l23.calculate(l11.output, l11.output)
l31.calculate(l21.output, l22.output)

# Printing output
print("Sum: " + str(l31.output))
print("Carry: " + str(l23.output))

