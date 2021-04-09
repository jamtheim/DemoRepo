
# Import section 
import random # Dont need this
import pandas # Dont need this


def ourFunction(number): 
    """
    This function takes a number and transforms to another

    parameters: number (float) 
    return: outNumber (float)
    
    """
    outNumber = number * 2
    return outNumber


number = 4
newNumber = ourFunction(number) 
print('Old number is ' + str(number))
print('New number is ' + str(newNumber))