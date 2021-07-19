"""following is an example for Inheritants. you can available a copy of all methods and variables of base class in 
subclass."""
"""and writened about over riding of constructor and function below. writened abort super"""

# Eg.

class BaseClass:

    # it is the cunstructor of BaseClass.if you created an object,then constructor's will work. here, there are two cunstructor one in Sub class and one here.then,at the time of object creation only work the cunstructor of sub class. If you want to work both constructors in Sub and Bse, you can use the keyword 'super' in sub class as below. If you use the keyword, then the constructor of Base will work.

    def __init__(self) -> None:  
        print( "from cunstructor of BaseClass.called me with keyword super" )

    def SetName( self , name ):
        self.name = name

        print( "welcome" )

    def Sample_over_riding_of_function( self ):

        print( "It is a sample function for test super in case of functon. from base" )

class Sub( BaseClass ):

    def __init__(self) -> None:

        print( "from cunstructor of Sub class" )
        super().__init__()   # here is the keyword 'super'. we called BaseClass's cunstructor at the time of calling of sub cunstructor.It is the method for call base cunstructor.

    def ShowName( self ):

        print( 'name is: '+self.name )

    def Sample_over_riding_of_function( self ):
        
        super().Sample_over_riding_of_function()

        print( "It is a sample function for test super in case of function. fro sub." )


x = Sub() # here we created an object in class 'Sub' 

x.SetName( "Abdhu" )
x.ShowName()
 # here we calle method 'ShowName' and 'SetName' from sub class. SetName is a method which writened in BaseClass , but we are calleed from sub class. but it is working . because it is inherited in to sub. if you inherit a class in to an onother one, the all methods and variables from base class will available in the sub class.

x.Sample_over_riding_of_function() # here, we are called only the method which writen in class sub. but there is writened a method in base class as same as the name of the sub class. here, working that two with one call. because, we are used the keyword 'super' for call that method from base.
