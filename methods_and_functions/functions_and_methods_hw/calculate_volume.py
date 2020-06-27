"""
This program is used to calculate the volume of a sphere
through the use of a function
"""

def vol(rad):
    """
    This function is used to take the  radius of a sphere and calculate
    its voloume using the equation (a/b)(Pi(r**3))
    """
    the_vol = lambda radius: (4/3)*(3.14159265359*(radius**3))
    return the_vol(rad)



#print(the_vol(2))
print(vol(2))
