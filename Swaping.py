num1 = int( input( "Enter 5 numbers you want to swap" ) )
num2 = int( input() )
num3 = int( input() )
num4 = int( input() )
num5 = int( input() )

n = num2
swap = num1
num1 = num5
num2 = num4
num3 = num3
num4 = n
num5 = swap

print( "result is " + str( num1 )+" " +str( num2 )+" " +str( num3 )+" " +str( num4 )+" " +str( num5 ))

