class Calculator:
    calculation_type = "Arithmetic Operations"

    #static method
    
    def add(a, b):

        return a + b
    
    #class method

    def multiply(cls, a , b):

        print(f"Calculation type: {cls.calculation_type}")
        return a * b