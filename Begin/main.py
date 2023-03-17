#code in Pyhton

                         
class Calculator:         #This calculator was made by a  Calculator class

    def __init__(self,num1, num2):           #Calculator class calculates numbers with mathematics accounts
        self.value_1 = num1
        self.value_2 = num2

    def sum(self):   
        return  self.value_1 + self.value_2       
        

    def dim(self):     
        return self.value_1 - self.value_2


    def multi(self):
        return self.value_1 * self.value_2


    def div(self):
        return self.value_1 / self.value_2

calculator = Calculator(10, 2)
print('The sum was: {}'.format(calculator.sum()))
print('The reduction was: {}'.format(calculator.dim()))
print('The multiplication was: {}'.format(calculator.multi()))
print('The division was: {}'.format(calculator.div()))


