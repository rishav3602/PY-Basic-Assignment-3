"""
9. How do you make a function variable refer to the global variable?
"""


"""
Answer...
We can make a function variable refer to the global variable just by adding a global keyword.


def myfunc():
  global x  #this will make a global variable.
  x = "Rishav"

myfunc()

print("Name is " + x)

"""