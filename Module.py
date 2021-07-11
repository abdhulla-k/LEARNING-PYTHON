import calculator   #it is an example of Module.every python files are modules.you can possible to import modules and use
# rom that module like below
calculator.substraction( 2, 3)

# possible to assign a function in to a variable and call that variable like below
cheque = calculator.ChequeNegativeOrPositive
cheque( -10 )

print( __name__ ) # it is using for find module name




from functionStudy import KeyWordAugumetn # this methods using for call only one function or something from a module.

"""in this case we are only calling a function from a module.onother functions and cods are including in that
 module .bult that does not work. because, we are only called function KeywordArgument"""
KeyWordAugumetn( str(20) ,str(10) )



""" it is a method for importing module.the name of module may be long, then use this method for change the name and 
use that changed short name. the key word 'as' is using for replace the name"""
import forLoop as n 
n.sum( 2, 2 )

from calculator import ChequeNegativeOrPositive as k# it is an example of calling only onef function from a module and changing of the name
k( -1 )

""" there are more libraries available with python to use with module.if you need libraries, you can google about
that.import and use as your like , eg. platform,etc.."""