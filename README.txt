This program was written in Python 3.7.4 on Pycharm IDE.
The file name containing the code is "PostFix.py".
The output is printed to the console.  The "word" variable
is used to store an expression to plug directly into the
logicalEval call parameter that is in the print statement.
The default inputs in the print statements follow the
expressions defined in the "Program 1 - Python.pdf" in
the same order.  The expected output is the answer I
calculated separately by hand.  The number after
"Actual result is:" is the return value of logicalEval
on the corresponding input.  The lists were converted
to strings to perform stack operations then converted
back into lists to avoid using built in methods.  Most
methods returned a stack, while some returned a top value
as well as a stack.  logicalEval only returned the global
tos value, which is the top of the main stack.