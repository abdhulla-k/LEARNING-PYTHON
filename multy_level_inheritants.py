# in python, you can possible the multy level inheritants like below:


class First():
    
    def display(self):
        print( "From first" )

class second( First ):

    def display(self):
        print( "From second" )

class Third( second ):
    
    def display_Third(self):
        print( "From third" )

x = Third()

x.display_Third()
x.display()
"""in this file, there are two method in one name that includeing seperate classes which inherited. we called that name. 
which display will work?
that discussed in file 'multiple_inheritants.py'."""


