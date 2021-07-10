def sum( num1,num2 ):
    result = num1 + num2
    return result


def substraction( num1, num2 ):
    result = num1 - num2
    return result



choice = int( input("Enter \n 1 for addition \n 2 for substraction" ))

if choice == 1 :
    
    number1 = int( input( "Enter two numbers" ))
    number2 = int( input( ))

    result = sum( number1, number2 )
    print( "result is:"+ str( result ))

elif choice == 2 :

    number1 = int( input( "Enter two numbers" ))
    number2 = int( input( ))

    result = substraction( number1, number2 )
    print( "result is:"+ str( result ))





