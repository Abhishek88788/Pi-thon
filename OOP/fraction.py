class Fraction:
    def __init__(self,n,d):
        self.numerator = n
        self.denominator = d
        # print(self)

    def __str__(self):
        return "{}/{}".format(self.numerator,self.denominator)
    
    def __add__(self,other):

        temp_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        temp_denominator = self.denominator * other.denominator
        
        return "{}/{}".format(temp_numerator,temp_denominator)
    
    def __sub__(self,other):

        temp_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        temp_denominator = self.denominator * other.denominator
        
        return "{}/{}".format(temp_numerator,temp_denominator)