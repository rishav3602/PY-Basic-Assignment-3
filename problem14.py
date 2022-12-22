"""
14. What is the purpose of the try clause? What is the purpose of the except clause?
"""


"""
Answer...

Try clause is the block in which we write the general code that may or may not have the
error. If the try clause has errors the program then goes to except block in which it is
given with codes to execute in the case if the codes in the try block has some errors.
Only one of the try or except block executes.

example:

try:
    with open("file.txt",'r') as f:
        print(f.read)

except File not found error as fe :
    print("The given file is not found")
    print(fe)

"""