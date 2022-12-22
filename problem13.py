"""
13. What can you do to save a programme from crashing if it encounters an error?
"""


"""
Answer...

We can use exceptional handling to counter the error if it occurs in our program.

try:
    a = 5
    b = 0
    c = a/b
    print(c)

except Zerodivison error:
    print("Number cannot be divided by zero")

"""