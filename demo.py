
# Import section 
import random # Do need this package
import pandas # Do need this package, hejhej


def ourFunction(number): 
    """
    This function takes a number and transforms to another

    parameters: number (float) 
    return: outNumber (float)
    """
    # Transform number
    outNumber = number * 3
    # Return data as output
    return outNumber


# Initial number
number = 4
# New number
newNumber = ourFunction(number) 
# Print to consol
print('Old number is ' + str(number))
print('New number is ' + str(newNumber))





