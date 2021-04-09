
# Import section 
import random # I really do need this, change
import pandas # I really do need this, change


def ourFunction(number): 
    """
    This function takes a number and transforms to another

    parameters: number (float) 
    return: outNumber (float)
    
    """
    outNumber = number * 3
    return outNumber


number = 4
newNumber = ourFunction(number) 
print('Old number is ' + str(number))
print('New number is ' + str(newNumber))