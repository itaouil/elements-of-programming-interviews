"""
   Convert an integer to a string.
"""

# function to convert from
# integer to string
def int_to_string(value):

    # Check if value is 0
    if value == 0:
        return "0"

    # Check if integer is <0
    is_negative = True if value < 0 else False

    # Ouput
    output = []

    # Build ouput string array
    if is_negative:
        output.append("-")

    # Get length of the value
    length = len(str(value))

    for x in range(length - 1, 0, -1):
        # Compute intermediate value
        temp = value // (10**x)

        # Populate array        
        output.append(str(temp))

        # Updae value
        value = value - temp * 10**x

    # Add last value
    output.append(str(value))

    print(output)

    # return string
    return "".join(output)

# Try
print(int_to_string(987))
print(int_to_string(9))
print(int_to_string(0))
