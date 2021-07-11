""" followint is an example of Exception. it is a type of error.not syntax error.want to solve exception errors as below """
b = int( input( "Enter a number" ))
a = int( input( ))

try:
    c = a / b
    print( c )

except ZeroDivisionError:

    print( "can't devided by zero" )

print( "Program finished" )