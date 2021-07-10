
def arbitrarryArgument( *values  ): # 'def' is a key word that using to define function
    #do you want to pass unlimitted argument, when use the key word "(* +name )".it is arbitrary argument

    print( "Result is from arbitrary argument:"+values[0]+values[1]+values[2]+values[3]+values[4]+values[5])
    # it is an example for adding values in to exicution from 'arbitrary argument'


arbitrarryArgument( "a","b","d","h","ulla","K")

""" it is an method of passing unlimited argument to function.an onother method is 'List'.already learned in List.py"""



result = 20
n = 30   



def GlobalAndLocalVariable():       # following code is an exampele of usage of global & local variables

    result = 10  

    """ here n and result that writen on out side of function are global 'variable'global variables 
    are avilabe both fin unction and otside of function."""

    print( "result is from global and local variable explained function:"+str( result ))

    """All variables that writen in the inside of the function is local variable.Local variables are only
    avilable in under of function """

    print( n )
    print( result )


GlobalAndLocalVariable()



def KeyWordAugumetn(name,age):# it is the example of keyword argument e.i in this option, there is no condition to pass argument in order
    print( "result from Keyword argument explained function: "+name, age ) # in this case the names are key words


KeyWordAugumetn( age=20, name="abdhu" )


def defaltArgument( name, age=10 ):# it is an exampe of defalt argument.

    """ age is already given,there for, if you pass only one argument, then defalt will work.
    If you pass two argument one to name and onother one to age defalted argument will change as passed. """


    print( age,name )


defaltArgument( "from function defalt argument: Abdhu" )

